import cv2
import numpy as np

while True:
    my_image = np.random.random((400, 600)) * 255
    my_image = np.array(my_image, dtype=np.uint8)

    cv2.imshow("", my_image)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
