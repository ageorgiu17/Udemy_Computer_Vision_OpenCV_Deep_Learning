# importing the libraries
import numpy as np
import cv2

# reading the image
image = cv2.imread("../DATA/dog_backpack.png")


# function that draws the circles
def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img=image, center=(x, y), radius=70, color=(255, 0, 0), thickness=4)


# connecting the function to the image
cv2.namedWindow("dog")
cv2.setMouseCallback("dog", draw_circle)


# showing the image
while True:
    cv2.imshow("dog", image)

    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()
