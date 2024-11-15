import cv2
import numpy as np


image = cv2.imread("Photo_Sketch/input/me.jpg")

image_inverted = 255 - image
image_blured = cv2.GaussianBlur(image_inverted, (21, 21), 0)
image_inverted_blure = 255 - image_blured

sketch = (image / image_inverted_blure) * 255

# cv2.imwrite("Photo_Sketch/output/image_inverted.jpg", image_inverted)
# cv2.imwrite("Photo_Sketch/output/image_blured.jpg", image_blured)
# cv2.imwrite("Photo_Sketch/output/image_inverted_blure.jpg", image_inverted_blure)
cv2.imwrite("Photo_Sketch/output/sketch.jpg", sketch)
