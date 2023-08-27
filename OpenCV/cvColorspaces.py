import cv2 as cv

img = cv.imread("C:\\Users\\Hp\\Downloads\\python_images\\Cat1.jpg")

# BGR TO GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# BGR TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# BGR TO LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

# BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow("org", img)
cv.imshow("gray", gray)
cv.imshow("hsv", hsv)
cv.imshow("lab", lab)
cv.imshow("rgb", rgb)

# RESERVE OPERATIONS

# HSV TO BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

# LAB TO BGR
Lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)

# RGB TO BGR
rgb_bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)

cv.imshow("hsv_bgr", hsv_bgr)
cv.imshow("lab_bgr", Lab_bgr)
cv.imshow("rgb_bgr", rgb_bgr)


cv.waitKey(0)
