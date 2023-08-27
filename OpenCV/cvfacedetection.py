import cv2 as cv


img = cv.imread("C:\\Users\\Hp\\Downloads\\python_images\\person.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

haar_cascade = cv.CascadeClassifier(
    "C:\\Users\\Hp\\Desktop\\Python\\Computer Vision\\haar_face.xml"
)

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

for (x, y, w, h) in face_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("Face Detected", img)
cv.waitKey(0)
