import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\Hp\\Downloads\\python_images\\Cat1.jpg")

# -ve x is left
# +ve x is Right
# -ve y is up
# +ve y is down


def translate(img, x, y):
    transmat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transmat, dimensions)


cv.imshow("Image", translate(img, 0, 0))


# Rotation


def rotate(img, angle, rotpoint=None):
    dimensions = (img.shape[1], img.shape[0])
    if rotpoint == None:
        rotpoint = (img.shape[1] // 2, img.shape[0] // 2)
    rotmar = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    return cv.warpAffine(img, rotmar, dimensions)


cv.imshow("Cat Roatated", rotate(img, 180))

# Flipping
# Flipping codes
# 1 flips horizontally
# 0 flips vertically
# -1 flips vertically and horizontally (180°)


flipped = cv.flip(img, -1)
cv.imshow("Flipped", flipped)


cv.waitKey(0)
