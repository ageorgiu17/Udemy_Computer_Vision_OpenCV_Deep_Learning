import numpy as np
import cv2

blank_image = np.zeros(shape=(512, 512, 3), dtype=np.int8)


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(
            img=blank_image, center=(x, y), radius=40, color=(0, 255, 0), thickness=-1
        )
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(
            img=blank_image, center=(x, y), radius=40, color=(0, 0, 255), thickness=-1
        )


cv2.namedWindow(winname="drawing2")
cv2.setMouseCallback("drawing2", draw_circle)

while True:
    cv2.imshow("drawing2", blank_image)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
