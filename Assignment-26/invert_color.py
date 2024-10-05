import cv2

# read image
image1 = cv2.imread("images/1.jpg")
image1_cvt = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

image2 = cv2.imread("images/2.jpg")
image2_cvt = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# invert dark and light images pixels
image1_neg = cv2.bitwise_not(image1_cvt)
image2_neg = cv2.bitwise_not(image2_cvt)

# save images
cv2.imwrite("images/1_cvt.jpg", image1_neg)
cv2.imwrite("images/2_cvt.jpg", image2_neg)
