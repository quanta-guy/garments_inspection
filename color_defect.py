import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('H','image',0,255,nothing)  # Hue is in the range 0-255
cv2.createTrackbar('S','image',0,255,nothing)
cv2.createTrackbar('V','image',0,255,nothing)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply Gaussian blur to reduce noise
    frame = cv2.GaussianBlur(frame, (5, 5), 0)

    # get current positions of trackbars    
    h = cv2.getTrackbarPos('H','image')
    s = cv2.getTrackbarPos('S','image')
    v = cv2.getTrackbarPos('V','image')

    # Define range of red color in HSV
    lower_bound = np.array([h-10, s, v])
    upper_bound = np.array([h+10, 255, 255])

    # Threshold the HSV image to get only red color
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Bitwise-AND mask and original image
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('image', result)

    if cv2.waitKey(1) & 0xFF == 27:   # Esc key to stop
        break

cap.release()
cv2.destroyAllWindows()
