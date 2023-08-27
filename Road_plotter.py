import struct

f = open("C:\\Users\\Hp\\Desktop\\Python\\roaddata.bmp", "rb")
wb = f.seek(18, 0)
width = struct.unpack("i", f.read(4))[0]
print(width)
height = struct.unpack("i", f.read(4))[0]
print(height)
f.seek(54, 0)
arr = []

for i in range(height):
    temp = []
    for j in range(width):
        red = int.from_bytes(f.read(1), "little", signed=False)
        blue = int.from_bytes(f.read(1), "little", signed=False)
        green = int.from_bytes(f.read(1), "little", signed=False)
        if red == 255 and blue == 255 and green == 255:
            temp.append(0)
        else:
            temp.append(1)
    arr.append(temp)


print(arr)
