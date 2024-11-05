import cv2
import numpy as np

hilari_gray = cv2.imread("input/hilari.png")
trump_gray = cv2.imread("input/trump.png")

hilari_gray = cv2.resize(hilari_gray,[502, 751])
trump_gray = cv2.resize(trump_gray, [502, 751])

hilari_gray = hilari_gray.astype(np.float32)
trump_gray = trump_gray.astype(np.float32)

img1 = hilari_gray * 3 / 4 + trump_gray * 1 / 4
img2 = hilari_gray * 2 / 4 + trump_gray * 2 / 4
img3 = hilari_gray * 1 / 4 + trump_gray * 3 / 4

img1 = img1.astype(np.uint8)
img2 = img2.astype(np.uint8)
img3 = img3.astype(np.uint8)

result = np.concatenate((hilari_gray, img1, img2, img3, trump_gray), axis=1)
cv2.imwrite("output/us.jpg", result)
