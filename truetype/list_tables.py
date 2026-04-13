import struct

with open("CompositeMS.ttf", "rb") as f:
    data = f.read()

# Offset table: sfVersion(4), numTables(2), searchRange(2), entrySelector(2), rangeShift(2)
sf_version, num_tables, search_range, entry_selector, range_shift = struct.unpack_from(">IHHHH", data, 0)

print(f"sfVersion: 0x{sf_version:08X}")
print(f"numTables: {num_tables}")
print()
print(f"{'Tag':<8} {'Checksum':>12} {'Offset':>10} {'Length':>10}")
print("-" * 46)

for i in range(num_tables):
    offset = 12 + i * 16
    tag = data[offset:offset+4].decode("ascii")
    checksum, table_offset, length = struct.unpack_from(">III", data, offset + 4)
    print(f"{tag:<8} 0x{checksum:08X} {table_offset:>10} {length:>10}")
