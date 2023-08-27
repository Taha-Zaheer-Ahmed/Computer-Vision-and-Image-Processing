import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\Hp\\Downloads\\python_images\\Cat1.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
blurforCanny = cv.GaussianBlur(gray, (3, 1), cv.BORDER_DEFAULT)

blank = np.zeros(img.shape, dtype="uint8")

cv.imshow("Blur", blur)

canny = cv.Canny(blurforCanny, 125, 175)
cv.imshow("Canny", canny)

ret, thresh = cv.threshold(blur, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank, contours, -1, (0, 255, 0), 2)
cv.imshow("Drawn contours", blank)


cv.waitKey(0)
