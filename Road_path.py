import struct


def roadplotter(image):
    image.seek(18, 0)
    width = struct.unpack("i", image.read(4))[0]
    print("width of image is : ", width)
    height = struct.unpack("i", image.read(4))[0]
    print("height of image is : ", height)
    image.seek(54, 0)
    arr = []

    for i in range(height):
        temp = []
        for j in range(width):
            red = int.from_bytes(image.read(1), "little", signed=False)
            blue = int.from_bytes(image.read(1), "little", signed=False)
            green = int.from_bytes(image.read(1), "little", signed=False)
            if red == 255 and blue == 255 and green == 255:
                temp.append(0)
            else:
                temp.append(1)
        arr.append(temp)

    return arr


def length(array):
    def blobcount(img, r, c):
        if r < len(img) and c < len(img[0]) and r != -1 and c != -1:
            if img[r][c] == 0:
                return 0
            else:
                img[r][c] = 0
                return (
                    1
                    + blobcount(img, r, c - 1)
                    + blobcount(img, r, c + 1)
                    + blobcount(img, r - 1, c - 1)
                    + blobcount(img, r - 1, c)
                    + blobcount(img, r - 1, c + 1)
                    + blobcount(img, r + 1, c - 1)
                    + blobcount(img, r + 1, c)
                    + blobcount(img, r + 1, c + 1)
                )
        else:
            return 0

    counter = 0
    for row in range(len(array)):
        for col in range(len(array[0])):
            if array[row][col] == 1:
                n = blobcount(array, row, col)
            else:
                continue
            print(f"Length of road { counter + 1} is {n} pixels")
            counter += 1


blueprint = open("C:\\Users\\Hp\\Desktop\\Python\\roaddata.bmp", "rb")
array = roadplotter(blueprint)
result = length(array)
