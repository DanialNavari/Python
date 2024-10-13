import cv2

image = cv2.imread("")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow(image_gray)
cv2.waitKey()