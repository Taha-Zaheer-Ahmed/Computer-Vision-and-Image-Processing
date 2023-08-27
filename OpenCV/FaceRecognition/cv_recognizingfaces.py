import os
import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier(
    "C:\\Users\\Hp\\Desktop\\Python\\Computer Vision\\haar_face.xml"
)
faces = []
for i in os.listdir(r"C:\\Users\\Hp\\Desktop\\Faces"):
    faces.append(i)
print(faces)
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read(
    "C:\\Users\\Hp\\Desktop\\Python\\Computer Vision\\Face_trained.yml"
)

img = cv.imread("C:\\Users\\Hp\\Desktop\\testfaces\\christesting\\christest2.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

for (x, y, w, h) in face_rect:
    face_roi = gray[y : y + h, x : x + w]
    label, confidence = face_recognizer.predict(face_roi)
    print(f"{faces[label]}'s face detected with confidence {confidence}%")
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv.putText(
        img,
        str(faces[label]),
        ((x + w // 2) - x // 2, y + h),
        cv.FONT_HERSHEY_COMPLEX,
        0.7,
        (0, 255, 0),
        2,
    )
    cv.imshow("Image", img)

cv.waitKey(0)
