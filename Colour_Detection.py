import cv2
import numpy as np


def empty():
    pass

## Colour Detection using trackbars
path = "Capture.png"
img = cv2.imread(path)


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 300)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 23, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 70, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 125, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("ImgOr", img)
    cv2.imshow("ImgHSV", imgHSV)
    cv2.imshow("ImgM", mask)
    cv2.imshow("ImgR", imgResult)
    cv2.waitKey(1)


