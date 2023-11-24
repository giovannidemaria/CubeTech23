import cv2
import numpy as np
from matplotlib import pyplot as plt

# reading image
img = cv2.imread('Target.jpeg')

# converting image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# setting threshold of gray image
# adjust threshold according to picamera brightness  ----
_, threshold = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

dim = (1024, 765)

resized = cv2.resize(threshold, dim, interpolation = cv2.INTER_AREA)

#modes maybe a faster one?? method simple for the inner none
contours, _ = cv2.findContours(resized, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

for contour in contours:

    # here we are ignoring first counter because
    # findcontour function detects whole image as shape
    if i == 0:
        i = 1
        continue

    # cv2.approxPloyDP() function to approximate the shape
    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)

    # using drawContours() function
    cv2.drawContours(resized, [contour], 0, (125, 125, 125), 5)

    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])

    if len(approx) == 4:
        cv2.putText(resized, 'Triangle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (60,60,60), 2)

cv2.imshow('shapes', resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
