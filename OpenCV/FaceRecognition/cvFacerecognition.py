import os
import cv2 as cv
import numpy as np

faces = []
dir = r"C:\\Users\\Hp\\Desktop\\Faces"

for i in os.listdir(r"C:\\Users\\Hp\\Desktop\\Faces"):
    faces.append(i)
print(faces)

haar_cascade = cv.CascadeClassifier(
    "C:\\Users\\Hp\\Desktop\\Python\\Computer Vision\\haar_face.xml"
)

features = []
labels = []


def create_train():
    for person in faces:
        path = os.path.join(dir, person)
        label = faces.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4
            )

            for (x, y, w, h) in face_rect:
                faces_roi = gray[y : y + h, x : x + w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print("Training done---------------")

features = np.array(features, dtype="object")
labels = np.array(labels)


face_recognizer = cv.face.LBPHFaceRecognizer_create()

# training the Recognizer
face_recognizer.train(features, labels)
face_recognizer.save("Face_trained.yml")


np.save("Features.npy", features)
np.save("labels.npy", labels)
