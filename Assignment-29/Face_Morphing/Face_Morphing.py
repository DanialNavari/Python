import cv2
import numpy as np

young = cv2.imread("Face_Morphing/input/young.png")
old = cv2.imread("Face_Morphing/input/old.png")

young_1 = cv2.resize(young, [502, 751])
old_2 = cv2.resize(old, [502, 751])

young_1 = young_1.astype(np.float32)
old_2 = old_2.astype(np.float32)

img1 = young_1 * 3 / 4 + old_2 * 1 / 4
img2 = young_1 * 2 / 4 + old_2 * 2 / 4
img3 = young_1 * 1 / 4 + old_2 * 3 / 4

img1 = img1.astype(np.uint8)
img2 = img2.astype(np.uint8)
img3 = img3.astype(np.uint8)

result = np.concatenate((young_1, img1, img2, img3, old_2), axis=1)
cv2.imwrite("Face_Morphing/output/us.jpg", result)
