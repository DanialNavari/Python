import cv2
import numpy as np

image_1 = cv2.imread("Secret/input/1.jpg")
image_2 = cv2.imread("Secret/input/2.jpg")

result = image_1 - image_2

cv2.imwrite("Secret/output/result.jpg", result)