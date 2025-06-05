import cv2
import numpy as np


def nothing(x):
    pass

def brightness_ctrl(img, bright):
    bar = bright - 127
    if bar >= 0:
        value = np.ones_like(img, dtype='uint8') * bar
        img_ctrl = cv2.add(img, value)
    else:
        value = np.ones_like(img, dtype='uint8') * (-bar)
        img_ctrl = cv2.subtract(img, value)
    return img_ctrl

   

cap = cv2.VideoCapture('./images/clip.mp4')

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

cv2.namedWindow('Brightness Control')
cv2.createTrackbar('Brightness', 'Brightness Control', 127, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Safely get brightness slider value
    bright = cv2.getTrackbarPos('Brightness', 'Brightness Control')

    # Apply brightness adjustment
    img_ctrl = brightness_ctrl(frame, bright)

    # Show the result
    cv2.imshow('Brightness Control', img_ctrl)

    if cv2.waitKey(20) == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()






