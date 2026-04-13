from dataclasses import dataclass
from pathlib import Path
import sys
import struct
from typing import Iterable


@dataclass
class GlyphTable:
    pass


@dataclass
class TrueType:
    sf_version: str
    glyf: GlyphTable


@dataclass
class Table:
    tag: str
    checksum: int
    offset: int
    length: int

    
def load_tables(data: bytes, num_tables: int) -> Iterable[Table]:
    for i in range(num_tables):
        offset = 12 + i * 16
        tag = data[offset:offset+4].decode("ascii")
        checksum, table_offset, length = struct.unpack_from(">III", data, offset + 4)
        yield Table(tag, checksum, table_offset, length)


def load_truetype(path: Path) -> TrueType:
    with open(path, "rb") as f:
        data = f.read()

        # Offset table: sfVersion(4), numTables(2), searchRange(2), entrySelector(2), rangeShift(2)
        sf_version, num_tables, search_range, entry_selector, range_shift = struct.unpack_from(">IHHHH", data, 0)

        tables = load_tables(data, num_tables)
        for table in tables:
            print(f"{table.tag:<8} 0x{table.checksum:08X} {table.offset:>10} {table.length:>10}")

    return TrueType(sf_version, glyf=GlyphTable())


def main():
    for arg in sys.argv[1:]:
        path = Path(arg)
        tt = load_truetype(path)
        

main()