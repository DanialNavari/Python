import cv2

bg = cv2.imread("images/gradient.jpg")
bg_cvt = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)

for i in range(255):
    bg_cvt[i : i + 1, 0:255] = abs(i - 255)
    cv2.imwrite("images/gradient_image.jpg", bg_cvt)
