# Threshold
import cv2 as cv

gray = cv.cvtColor(
    cv.imread("C:\\Users\\Hp\\Downloads\\python_images\\person.jpg"), cv.COLOR_BGR2GRAY
)
cv.imshow("Gray", gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)
cv.imshow("Threshold simple", thresh)

# Inverse Thresholding
threshold, thresh_inv = cv.threshold(gray, 120, 255, cv.THRESH_BINARY_INV)
cv.imshow("Threshold inverse", thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 3
)
cv.imshow("Adaptive Threshold", adaptive_thresh)

cv.waitKey(0)
