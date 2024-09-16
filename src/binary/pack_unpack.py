import struct

fmt = "ii"
x = 32
y = 5678

binary = struct.pack(fmt, x, y)
print(binary)

normal = struct.unpack(fmt, binary)
print(normal)


print(struct.pack("3i", 1, 2, 3))
print(struct.pack("5s", bytes("hello", "utf-8")))
print(struct.pack("5s", bytes("a longer string", "utf-8")))


for format in ["4s", "3i4s5d"]:
    print(f"format '{format}' needs {struct.calcsize(format)} bytes")