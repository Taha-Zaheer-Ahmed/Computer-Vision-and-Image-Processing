import struct

img = open("C:\\Users\\Hp\\Downloads\\HouseStarkShield1.bmp", "r+b")
print(img.read(1))
print(img.read(1))
img.seek(18, 0)
width = struct.unpack("i", img.read(4))[0]
height = struct.unpack("i", img.read(4))[0]
img.seek(10, 0)
offset = struct.unpack("i", img.read(4))[0]
img.seek(offset, 0)
for i in range(width):
    for j in range(height):
        b, g, r = img.read(1), img.read(1), img.read(1)
        b = int(255 - int.from_bytes(b, "little")).to_bytes(1, "little")
        g = int(255 - int.from_bytes(g, "little")).to_bytes(1, "little")
        r = int(255 - int.from_bytes(r, "little")).to_bytes(1, "little")
        img.seek(offset, 0)
        img.write(b), img.write(g), img.write(r)
        offset += 3
