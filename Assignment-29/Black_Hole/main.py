import os
import cv2
import numpy as np


def concat_final_image(image_1, image_2, image_3, image_4):
    image_1 = image_1.astype(np.float32)
    image_2 = image_2.astype(np.float32)
    image_3 = image_3.astype(np.float32)
    image_4 = image_4.astype(np.float32)

    result1 = np.concatenate((image_1, image_2), axis=1)
    result2 = np.concatenate((image_3, image_4), axis=1)
    result = result2 = np.concatenate((result1, result2), axis=0)
    result = result.astype(np.uint8)

    cv2.imwrite("Black_Hole/output/result.jpg", result)


def reduce_noise():
    dir_num = 4

    for i in range(dir_num):
        img_1 = cv2.imread(f"Black_Hole/input/{i+1}/1.jpg")
        img_2 = cv2.imread(f"Black_Hole/input/{i+1}/2.jpg")
        img_3 = cv2.imread(f"Black_Hole/input/{i+1}/3.jpg")
        img_4 = cv2.imread(f"Black_Hole/input/{i+1}/4.jpg")
        img_5 = cv2.imread(f"Black_Hole/input/{i+1}/5.jpg")

        img_1 = img_1.astype(np.float32)
        img_2 = img_2.astype(np.float32)
        img_3 = img_3.astype(np.float32)
        img_4 = img_4.astype(np.float32)
        img_5 = img_5.astype(np.float32)

        result = (img_1 + img_2 + img_3 + img_4 + img_5) / 5
        result = result.astype(np.uint8)
        cv2.imwrite(f"Black_Hole/output/result_{i+1}.jpg", result)


reduce_noise()

image_1 = cv2.imread("Black_Hole/output/result_1.jpg")
image_2 = cv2.imread("Black_Hole/output/result_2.jpg")
image_3 = cv2.imread("Black_Hole/output/result_3.jpg")
image_4 = cv2.imread("Black_Hole/output/result_4.jpg")

concat_final_image(image_1, image_2, image_3, image_4)
