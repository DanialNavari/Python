# improt library
import cv2
import random
import time
from PIL import Image

# read image
image = cv2.imread("image/snowfall.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
frames = []

def reset_image():
    image = cv2.imread("image/snowfall.jpg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# image shape = 1000 * 800
while True:
    for _ in range(400):
        snow_place_row = random.randint(0, 1000)
        snow_place_col = random.randint(0, 800)
        cv2.circle(image, (snow_place_row, snow_place_col), 1, 250, 2)

    # save random tv noise
    obj = time.localtime()
    if obj[5] % 2 == 0:
        cv2.imwrite("image/land1.jpg", image)
    elif obj[5] % 3 == 0:
        cv2.imwrite("image/land2.jpg", image)
    else:
        cv2.imwrite("image/land3.jpg", image)


    cv2.imshow("", image)
    cv2.waitKey(1)
    
    image = cv2.imread("image/snowfall.jpg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        
        # press q and quit programm and save gif
        frames.append(Image.open("image/land1.jpg"))
        frames.append(Image.open("image/land2.jpg"))
        frames.append(Image.open("image/land3.jpg"))
        frames[0].save(
            "image/snowfall.gif",
            format="GIF",
            append_images=frames[1:],
            save_all=True,
            duration=100,
            loop=0,
        )
        break
