# import library
import cv2
import time
import numpy as np
from PIL import Image

# read image
image = cv2.imread("image/tv.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
frames = []

while True:
    # make noise
    noise = np.random.random((165, 295)) * 255
    noise = np.array(noise, dtype=np.uint8)
    image[42:207, 177:472] = noise
    cv2.imshow("", image)

    # save random tv noise
    obj = time.localtime()
    if obj[5] % 2 == 0:
        cv2.imwrite("image/frame1.jpg", image)
    elif obj[5] % 3 == 0:
        cv2.imwrite("image/frame2.jpg", image)
    else:
        cv2.imwrite("image/frame3.jpg", image)

    # press q and quit programm and save gif
    if cv2.waitKey(1) & 0xFF == ord("q"):
        frames.append(Image.open("image/frame1.jpg"))
        frames.append(Image.open("image/frame2.jpg"))
        frames.append(Image.open("image/frame3.jpg"))
        frames.append(Image.open("image/frame4.jpg"))
        frames[0].save(
            "image/tv.gif",
            format="GIF",
            append_images=frames[1:],
            save_all=True,
            duration=100,
            loop=0,
        )
        break
