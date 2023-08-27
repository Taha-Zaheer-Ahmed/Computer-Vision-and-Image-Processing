# Histogram Computations
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# For Grayscale images
img = cv.imread("C:\\Users\\Hp\\Downloads\\python_images\\person.jpg")
cv.imshow("Original Image", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blank = np.zeros(img.shape[:2], dtype="uint8")
mask = cv.circle(blank.copy(), (200, 120), 85, 255, -1)

maskedgray = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow("Masked Gray-scale", maskedgray)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked Original", masked)

gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure()
plt.plot(gray_hist)
plt.title("Gray-Scale Plot")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.xlim((0, 256))

# For RGB Images

plt.figure()
plt.title("BGR Plot")
plt.xlabel("Bins")
plt.ylabel("# of pixels")

colors = ("b", "g", "r")
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim((0, 256))

plt.show()

cv.waitKey(0)
