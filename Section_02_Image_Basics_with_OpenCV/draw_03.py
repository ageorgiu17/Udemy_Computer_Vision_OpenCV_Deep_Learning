import numpy as np
import cv2

blank_image = np.zeros(shape=(512, 512, 3), dtype=np.int8)

## Variables
drawing = False
ix, iy = -1, -1


## Function
def draw_circle(event, x, y, flags, param):
    global drawing, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(
                img=blank_image,
                pt1=(ix, iy),
                pt2=(x, y),
                color=(0, 255, 0),
                thickness=-1,
            )
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(
            img=blank_image,
            pt1=(ix, iy),
            pt2=(x, y),
            color=(0, 255, 0),
            thickness=-1,
        )


## Image shown
cv2.namedWindow(winname="drawing2")
cv2.setMouseCallback("drawing2", draw_circle)

while True:
    cv2.imshow("drawing2", blank_image)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
