import cv2

image3 = cv2.imread("images/3.jpg")
image3_rotate = cv2.rotate(image3, cv2.ROTATE_180)

cv2.imwrite("images/3_rotate.jpg", image3_rotate)
