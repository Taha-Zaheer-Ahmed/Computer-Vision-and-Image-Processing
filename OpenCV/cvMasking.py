# Masking
import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\Hp\\Downloads\\python_images\\person.jpg")
blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("main", img)

circle = cv.circle(blank, (200, 125), 85, 255, -1)
cv.imshow("circle", circle)

mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow("mask", mask)

cv.waitKey(0)
