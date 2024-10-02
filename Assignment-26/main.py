import cv2

my_image = cv2.imread("image.jpg")
my_image_2 = cv2.cvtColor(my_image, cv2.COLOR_RGB2GRAY)
cv2.imshow("", my_image_2)
cv2.waitKey()
cv2.imwrite("result.jpg", my_image_2)
