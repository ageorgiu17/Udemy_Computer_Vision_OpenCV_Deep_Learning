import numpy as np
import cv2

blank_image = np.zeros(shape=(512, 512, 3), dtype=np.int8)

def draw_circle(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        cv2.circle(img=blank_image, center=(x, y), radius=40, color=(102, 255, 255), thickness=-1)

cv2.namedWindow(winname='drawing')
cv2.setMouseCallback('drawing', draw_circle)


while True:

    cv2.imshow('drawing', blank_image)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()