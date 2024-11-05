import cv2
import numpy as np

image_lion = cv2.imread("input/lion.jpg")
image_me = cv2.imread("input/sajjad.jpg")
 
image_me = cv2.cvtColor(image_me, cv2.COLOR_BGR2GRAY)
image_lion = cv2.cvtColor(image_lion, cv2.COLOR_BGR2GRAY)

image_me = image_me.astype(np.float32)
image_lion = image_lion.astype(np.float32)

result = image_me * 3 / 4  + image_lion /4
result = result.astype(np.uint8)

# result = cv2.add(image_me, image_lion)

cv2.imwrite("output/result.jpg", result)
