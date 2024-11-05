import cv2
import numpy as np

image_fanar = cv2.imread("input/e.tif")

image_fanar = cv2.cvtColor(image_fanar, cv2.COLOR_BGR2GRAY)
image_black = np.zeros(image_fanar.shape)

result = image_fanar - image_black
result = 255 - result
cv2.imwrite("output/fanar.jpg", result)
