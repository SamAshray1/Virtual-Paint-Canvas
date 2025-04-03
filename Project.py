import cv2
import numpy as np

def empty(a):
    pass

# Load image
path = "Capture.png"
img = cv2.imread(path)

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Create trackbars for HSV range adjustments
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 300)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    # Read frame from webcam
    success, frame = cap.read()
    if not success:
        break

    # Convert both to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)   # For Image
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # For Webcam

    # Get trackbar positions
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    # Define HSV range
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Create mask for both image & webcam feed
    mask_img = cv2.inRange(imgHSV, lower, upper)
    mask_frame = cv2.inRange(frameHSV, lower, upper)

    # Apply mask
    filtered_img = cv2.bitwise_and(img, img, mask=mask_img)
    filtered_frame = cv2.bitwise_and(frame, frame, mask=mask_frame)

    # Show results
    cv2.imshow("Original Image", img)
    cv2.imshow("Filtered Image", filtered_img)
    cv2.imshow("Webcam Feed", frame)
    cv2.imshow("Filtered Webcam", filtered_frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
