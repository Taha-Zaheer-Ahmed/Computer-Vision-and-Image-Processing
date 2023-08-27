# Edges
import cv2 as cv
import numpy as np

gray = cv.cvtColor(
    cv.imread("C:\\Users\\Hp\\Downloads\\python_images\\person.jpg"), cv.COLOR_BGR2GRAY
)
cv.imshow("Gray", gray)

# Laplacian Edge detection

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

# Sobel Edge detection

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobelxy = cv.bitwise_or(sobelx, sobely)

cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)
cv.imshow("Sobel XY", sobelxy)

# Canny edge detection

canny = cv.Canny(gray, 125, 175)
cv.imshow("Canny", canny)


cv.waitKey(0)
