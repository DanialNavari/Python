import time
import cv2

image = cv2.imread("image/bat.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshId = 100

_, image = cv2.threshold(image, threshId, 255, cv2.THRESH_BINARY_INV)
cv2.putText(image, "BATMAN", (400,450), cv2.FONT_HERSHEY_TRIPLEX, 1, 255, 1)
cv2.imshow("", image)
cv2.waitKey()
