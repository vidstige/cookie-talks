from dataclasses import dataclass
from pathlib import Path
import sys
import struct

@dataclass
class Point:
    x: int
    y: int
    on_curve: bool


@dataclass
class Contour:
    points: list[Point]


@dataclass
class Glyph:
    x_min: int
    y_min: int
    x_max: int
    y_max: int
    contours: list[Contour]


@dataclass
class Component:
    glyph_index: int
    x: int
    y: int


@dataclass
class CompositeGlyph:
    x_min: int
    y_min: int
    x_max: int
    y_max: int
    components: list[Component]




@dataclass
class HeadTable:
    index_to_loc_format: int


@dataclass
class MaxpTable:
    num_glyphs: int


@dataclass
class LocaTable:
    offsets: list[int]


@dataclass
class TrueType:
    sf_version: str
    cmap: dict[str, int]
    glyf: list[Glyph | CompositeGlyph | None]


@dataclass
class Table:
    checksum: int
    data: bytes


def load_tables(data: bytes, num_tables: int) -> dict[str, Table]:
    tables = {}
    for i in range(num_tables):
        entry = 12 + i * 16
        tag = data[entry:entry+4].decode("ascii")
        checksum, offset, length = struct.unpack_from(">III", data, entry + 4)
        tables[tag] = Table(checksum, data[offset:offset+length])
    return tables


def parse_glyph(data: bytes, offset: int, num_contours: int, x_min: int, y_min: int, x_max: int, y_max: int) -> Glyph:
    end_pts = struct.unpack_from(f">{num_contours}H", data, offset)
    offset += num_contours * 2

    instruction_length = struct.unpack_from(">H", data, offset)[0]
    offset += 2 + instruction_length

    num_points = end_pts[-1] + 1

    # Parse flags (with repeat)
    ON_CURVE  = 0x01
    X_SHORT   = 0x02
    Y_SHORT   = 0x04
    REPEAT    = 0x08
    X_SAME_OR_POS = 0x10
    Y_SAME_OR_POS = 0x20

    flags = []
    while len(flags) < num_points:
        flag = data[offset]; offset += 1
        flags.append(flag)
        if flag & REPEAT:
            repeat = data[offset]; offset += 1
            flags.extend([flag] * repeat)

    def read_coords(short_bit: int, same_or_pos_bit: int) -> list[int]:
        nonlocal offset
        coords, value = [], 0
        for flag in flags:
            if flag & short_bit:
                delta = data[offset]; offset += 1
                value += delta if (flag & same_or_pos_bit) else -delta
            elif flag & same_or_pos_bit:
                pass  # delta is 0
            else:
                delta = struct.unpack_from(">h", data, offset)[0]; offset += 2
                value += delta
            coords.append(value)
        return coords

    xs = read_coords(X_SHORT, X_SAME_OR_POS)
    ys = read_coords(Y_SHORT, Y_SAME_OR_POS)

    contours = []
    prev_end = -1
    for end in end_pts:
        points = [Point(xs[i], ys[i], bool(flags[i] & ON_CURVE)) for i in range(prev_end + 1, end + 1)]
        contours.append(Contour(points))
        prev_end = end

    return Glyph(x_min, y_min, x_max, y_max, contours)


def parse_composite_glyph(data: bytes, offset: int, x_min: int, y_min: int, x_max: int, y_max: int) -> CompositeGlyph:
    ARG_1_AND_2_ARE_WORDS = 0x0001
    ARGS_ARE_XY_VALUES    = 0x0002
    WE_HAVE_A_SCALE       = 0x0008
    MORE_COMPONENTS       = 0x0020
    WE_HAVE_AN_X_AND_Y_SCALE = 0x0040
    WE_HAVE_A_TWO_BY_TWO  = 0x0080

    components = []
    while True:
        flags, glyph_index = struct.unpack_from(">HH", data, offset)
        offset += 4

        if flags & ARG_1_AND_2_ARE_WORDS:
            arg1, arg2 = struct.unpack_from(">hh", data, offset)
            offset += 4
        else:
            arg1, arg2 = struct.unpack_from(">bb", data, offset)
            offset += 2

        x, y = (arg1, arg2) if (flags & ARGS_ARE_XY_VALUES) else (0, 0)
        components.append(Component(glyph_index, x, y))

        if flags & WE_HAVE_A_SCALE:
            offset += 2
        elif flags & WE_HAVE_AN_X_AND_Y_SCALE:
            offset += 4
        elif flags & WE_HAVE_A_TWO_BY_TWO:
            offset += 8

        if not (flags & MORE_COMPONENTS):
            break

    return CompositeGlyph(x_min, y_min, x_max, y_max, components)


def parse_cmap(table: Table) -> dict[str, int]:
    num_subtables = struct.unpack_from(">H", table.data, 2)[0]

    # Prefer platform 3 encoding 1 (Windows Unicode BMP), fall back to any format 4
    subtable_offset = None
    for i in range(num_subtables):
        platform_id, encoding_id, offset = struct.unpack_from(">HHI", table.data, 4 + i * 8)
        if struct.unpack_from(">H", table.data, offset)[0] == 4:
            subtable_offset = offset
            if (platform_id, encoding_id) == (3, 1):
                break  # best match, stop looking

    if subtable_offset is None:
        return {}

    seg_count_x2 = struct.unpack_from(">H", table.data, subtable_offset + 6)[0]
    seg_count = seg_count_x2 // 2

    base = subtable_offset + 14  # skip format, length, language, segCountX2, searchRange, entrySelector, rangeShift
    end_codes   = struct.unpack_from(f">{seg_count}H", table.data, base); base += seg_count * 2 + 2  # +2 reserved pad
    start_codes = struct.unpack_from(f">{seg_count}H", table.data, base); base += seg_count * 2
    id_deltas   = struct.unpack_from(f">{seg_count}h", table.data, base); base += seg_count * 2
    range_offsets_base = base
    id_range_offsets = struct.unpack_from(f">{seg_count}H", table.data, base)

    mapping = {}
    for i in range(seg_count):
        start, end = start_codes[i], end_codes[i]
        if start == 0xFFFF:
            break
        for c in range(start, end + 1):
            if id_range_offsets[i] == 0:
                glyph_id = (c + id_deltas[i]) & 0xFFFF
            else:
                pos = range_offsets_base + i * 2 + id_range_offsets[i] + (c - start) * 2
                glyph_id = struct.unpack_from(">H", table.data, pos)[0]
                if glyph_id != 0:
                    glyph_id = (glyph_id + id_deltas[i]) & 0xFFFF
            if glyph_id != 0:
                mapping[chr(c)] = glyph_id
    return mapping


def parse_head(table: Table) -> HeadTable:
    # indexToLocFormat is at byte offset 50 within the head table
    index_to_loc_format = struct.unpack_from(">h", table.data, 50)[0]
    return HeadTable(index_to_loc_format)


def parse_maxp(table: Table) -> MaxpTable:
    num_glyphs = struct.unpack_from(">H", table.data, 4)[0]
    return MaxpTable(num_glyphs)


def parse_loca(table: Table, head: HeadTable, maxp: MaxpTable) -> LocaTable:
    n = maxp.num_glyphs + 1
    if head.index_to_loc_format == 0:
        raw = struct.unpack_from(f">{n}H", table.data, 0)
        offsets = [v * 2 for v in raw]
    else:
        offsets = list(struct.unpack_from(f">{n}I", table.data, 0))
    return LocaTable(offsets)


def parse_glyf(table: Table, loca: LocaTable) -> list[Glyph | CompositeGlyph | None]:
    glyphs = []
    for i in range(len(loca.offsets) - 1):
        start, end = loca.offsets[i], loca.offsets[i + 1]
        if start == end:
            glyphs.append(None)  # empty glyph (e.g. space)
            continue

        pos = start
        num_contours, x_min, y_min, x_max, y_max = struct.unpack_from(">hhhhh", table.data, pos)
        pos += 10

        if num_contours >= 0:
            glyphs.append(parse_glyph(table.data, pos, num_contours, x_min, y_min, x_max, y_max))
        else:
            glyphs.append(parse_composite_glyph(table.data, pos, x_min, y_min, x_max, y_max))

    return glyphs


def load_truetype(path: Path) -> TrueType:
    with open(path, "rb") as f:
        data = f.read()

    sf_version, num_tables, *_ = struct.unpack_from(">IHHHH", data, 0)
    tables = load_tables(data, num_tables)

    cmap = parse_cmap(tables["cmap"])
    head = parse_head(tables["head"])
    maxp = parse_maxp(tables["maxp"])
    loca = parse_loca(tables["loca"], head, maxp)
    glyf = parse_glyf(tables["glyf"], loca)
    return TrueType(sf_version, cmap=cmap, glyf=glyf)


def main():
    for arg in sys.argv[1:]:
        path = Path(arg)
        tt = load_truetype(path)
        print(f"\n{len(tt.glyf)} glyphs loaded")
        for i, g in enumerate(tt.glyf):
            if g is None:
                print(f"  [{i}] <empty>")
            elif isinstance(g, Glyph):
                print(f"  [{i}] Simple  bbox=({g.x_min},{g.y_min},{g.x_max},{g.y_max}) contours={len(g.contours)}")
            elif isinstance(g, CompositeGlyph):
                refs = [c.glyph_index for c in g.components]
                print(f"  [{i}] Composite bbox=({g.x_min},{g.y_min},{g.x_max},{g.y_max}) components={refs}")


main()
