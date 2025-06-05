
import numpy as np
import cv2

# %%
img = cv2.imread('./images/character.png')
img = cv2.resize(img,(300,300),interpolation=cv2.INTER_AREA)
cv2.imshow('Original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# %% [markdown]
# # Controlling Brightness of Image

# %%
def nothing(x):
    pass
cv2.namedWindow('Brightness Control')
bright = cv2.createTrackbar('Brightness','Brightness Control',75,255,nothing) # slider starts at 75
value = np.ones_like(img,dtype='uint8')

while True:
    
    bright = cv2.getTrackbarPos('Brightness','Brightness Control')
    bar = bright - 127  # You subtract 127 to shift the center to 0.

    if bar >= 0:
        value = np.ones_like(img,dtype='uint8') * bar
        img_ctrl = cv2.add(img, value)

    else:
        bright = 127 - bright
        value = np.ones_like(img,dtype='uint8') * bright
        img_ctrl = cv2.subtract(img, value)

    cv2.imshow('Brightness Control', img_ctrl)

    if cv2.waitKey(1) == 27:  # esc button
        break

cv2.destroyAllWindows()




