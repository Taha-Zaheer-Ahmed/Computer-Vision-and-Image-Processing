import cv2 as cv
import numpy as np

gray = cv.cvtColor(
    cv.imread("C:\\Users\\Hp\\Downloads\\python_images\\person.jpg"), cv.COLOR_BGR2GRAY
)
cv.imshow("Gray", gray)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

threshold, thresh = cv.threshold(lap, 30, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

cv.waitKey(0)
