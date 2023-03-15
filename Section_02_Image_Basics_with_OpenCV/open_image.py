import cv2

image = cv2.imread("../DATA/00-puppy.jpg")

while True:
    cv2.imshow("Puppy", image)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
