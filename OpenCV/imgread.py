import cv2 as cv

# For images
img = cv.imread("C:\\Users\\Hp\\Downloads\\python_images\\Cat2.jpg")

cv.imshow("Catter", img)
print(img)

cv.waitkey(20)

# For Videos
video = cv.VideoCapture("C:\\Users\\Hp\\Downloads\\python_images\\Dog.mp4")

while True:
    isTrue, Frame = video.read()
    cv.imshow("Video", Frame)

    if cv.waitKey(20) and 0xFF == ord("d"):
        break

video.release()
cv.destroyAllWindows()
