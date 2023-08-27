import struct
from math import floor


def Keepinrange(value):
    if value < 0:
        return 0
    elif value > 255:
        return 255
    else:
        return value


def convolution(color, kernel, r, c):
    colorconv = (
        (kernel[0][0] * color[r - 1][c - 1])
        + (kernel[0][1] * color[r - 1][c])
        + (kernel[0][2] * color[r - 1][c + 1])
        + (kernel[1][0] * color[r][c - 1])
        + (kernel[1][1] * color[r][c])
        + (kernel[1][2] * color[r][c + 1])
        + (kernel[2][0] * color[r + 1][c - 1])
        + (kernel[2][1] * color[r + 1][c])
        + (kernel[2][2] * color[r + 1][c + 1])
    )
    return floor(colorconv)


img = open(f"C:\\Users\\Hp\\Downloads\\python_images\\HouseStarkShield4.BMP", "r+b")
img.seek(18, 0)
width = struct.unpack("i", img.read(4))[0]
height = struct.unpack("i", img.read(4))[0]
img.seek(10, 0)
offset = struct.unpack("i", img.read(4))[0]
blue = []
green = []
red = []
img.seek(offset, 0)
for i in range(height):
    bluetemp = []
    greentemp = []
    redtemp = []
    for j in range(width):
        bluetemp.append(int.from_bytes(img.read(1), "little"))
        greentemp.append(int.from_bytes(img.read(1), "little"))
        redtemp.append(int.from_bytes(img.read(1), "little"))
    blue.append(bluetemp)
    green.append(greentemp)
    red.append(redtemp)
kernel = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
img.seek(offset, 0)
for r in range(height):
    for c in range(width):
        if (r == 0 or r == height - 1) or (c == 0 or c == width - 1):
            b = int(blue[r][c]).to_bytes(1, "little")
            g = int(green[r][c]).to_bytes(1, "little")
            r_ed = int(red[r][c]).to_bytes(1, "little")
            img.write(b)
            img.write(g)
            img.write(r_ed)
        else:
            blueconv = Keepinrange(convolution(blue, kernel, r, c))
            greenconv = Keepinrange(convolution(green, kernel, r, c))
            redconv = Keepinrange(convolution(red, kernel, r, c))
            img.write(blueconv), img.write(greenconv), img.write(redconv)
