import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\Hp\\Downloads\\python_images\\Cat.jpg")
b, g, r = cv.split(img)

blank = np.zeros(img.shape[:2], dtype="uint8")


merged = cv.merge([b, g, r])
cv.imshow("merged", merged)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)


cv.waitKey(0)
