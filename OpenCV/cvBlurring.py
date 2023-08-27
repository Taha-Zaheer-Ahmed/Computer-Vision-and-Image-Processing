# Blurring techniques
import cv2 as cv

img = cv.imread("C:\\Users\\Hp\\Downloads\\python_images\\Cat.jpg")

# Averaging
meanBlur = cv.blur(img, (7, 7), cv.BORDER_DEFAULT)
# Gaussian Blur
gaussianblur = cv.GaussianBlur(img, (7, 7), 0)
# Median Blur
medianblur = cv.medianBlur(img, 3)
# Bilateral Filter
bilateral = cv.bilateralFilter(medianblur, 45, 45, 45)

cv.imshow("Original", img)
cv.imshow("Averaging", meanBlur)
cv.imshow("Gaussian Blur", gaussianblur)
cv.imshow("meadian blur", medianblur)
cv.imshow("bilteral filter", bilateral)

imgcanny = cv.Canny(img, 125, 175)
bilateralcanny = cv.Canny(bilateral, 125, 175)

cv.imshow("Original Cannny", imgcanny)
cv.imshow("bilteral filter Canny", bilateralcanny)


cv.waitKey(0)
