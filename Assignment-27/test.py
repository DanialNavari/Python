import cv2
import numpy as np

my_image = np.ones((500, 800), dtype=np.uint8) * 255
cv2.rectangle(my_image, (30,35), (410,350), 128, 20)
cv2.circle(my_image, (600,200), 100, 120, 10)
cv2.line(my_image, (100,100), (700,150), 180, 15)
cv2.putText(my_image, "Danielnv", (400,250), cv2.FONT_HERSHEY_COMPLEX, 1,100)
# my_image = np.random.random((250, 350)) * 255
# my_image = np.array(my_image, dtype=np.uint8)

cv2.imshow("", my_image)
cv2.waitKey()
