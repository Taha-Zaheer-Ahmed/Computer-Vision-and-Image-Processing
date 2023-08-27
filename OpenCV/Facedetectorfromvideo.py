import cv2 as cv

vid = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier(
    "C:\\Users\\Hp\\Desktop\\Python\\Computer Vision\\haar_face.xml"
)
while True:
    isTure, frame = vid.read()
    framegray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_rect = haar_cascade.detectMultiScale(
        framegray, scaleFactor=1.1, minNeighbors=3
    )
    # print(f"Faces detected {len(face_rect)}")
    for (x, y, w, h) in face_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv.imshow("Video", frame)

    if cv.waitKey(20) and 0xFF == ord("d"):
        break

vid.release()
cv.destroyAllWindows()
