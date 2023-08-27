# Bitwise operations
import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# Bitwise AND --> for intersecting Areas
bitwise_and = cv.bitwise_and(rectangle, circle)

# Bitwise OR --> for intersecting and non-intersecting Areas
bitwise_or = cv.bitwise_or(rectangle, circle)

# Bitwise XOR --> for non-intersecting Areas
bitwise_xor = cv.bitwise_xor(rectangle, circle)

# Bitwise NOT --> for inverting image
bitwise_not = cv.bitwise_not(rectangle)

cv.imshow("Bitwise AND", bitwise_and)
cv.imshow("Bitwise OR", bitwise_or)
cv.imshow("Bitwise XOR", bitwise_xor)
cv.imshow("Bitwise NOT", bitwise_not)

cv.waitKey(0)
