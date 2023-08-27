import cv2 as cv

img = cv.imread("C:\\Users\\Hp\\Downloads\\python_images\\Cat.jpg")
cv.imshow("Original", img)

# GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# BLur
Blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("Blur", Blur)

# Edge Cascade
edge = cv.Canny(Blur, 0, 75)
cv.imshow("Edge", edge)

# dialation
dialate = cv.dilate(edge, (7, 7), iterations=1)
cv.imshow("Dialate", dialate)

# Erosion/Inverse Dialation
eroded = cv.erode(dialate, (7, 7), iterations=1)
cv.imshow("Eroded", eroded)

# Croppoing
Cropped = img[50:200, 200:400]
cv.imshow("Cropped", Cropped)


cv.waitKey(0)

vid = cv.VideoCapture("C:\\Users\\Hp\\Downloads\\python_images\\30.mp4")

while True:
    isTrue, Frame = vid.read()
    frameblur = cv.GaussianBlur(Frame, (3, 3), cv.BORDER_DEFAULT)
    frameedge = cv.Canny(frameblur, 125, 175)
    framdialated = cv.dilate(frameedge, (3, 3), iterations=3)
    cv.imshow("Vid", framdialated)

    if cv.waitKey(20) and 0xFF == ord("d"):
        break

vid.release()
cv.destroyAllWindows()
