import cv2 as cv


def resizeframe(frame, scale=0.30):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


video = cv.VideoCapture(0)

while True:
    isTrue, frame = video.read()
    frameresize = resizeframe(frame)
    cv.imshow("Video", frame)
    cv.imshow("Resized", frameresize)

    if cv.waitKey(20) and 0xFF == ord("d"):
        break

video.release()
cv.destroyAllWindows
