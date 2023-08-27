import cv2 as cv
import numpy as np
import math

blank = np.zeros((500, 500, 3), dtype="uint8")
# cv.imshow("Blank", blank)

# blank[:] = 0, 255, 0
# cv.imshow("green", blank)

# cv.circle(blank, (250, 250), 250, (255, 0, 0), -2)
# cv.imshow("image", blank)

# Writing text
cv.putText(
    blank, "Hello Batman", (150, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2
)
cv.imshow("Text", blank)

cv.waitKey(0)
