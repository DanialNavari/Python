# import library
import cv2

# read images
home = cv2.imread("Virtual_Decorate/input/home.jpg")
decore = cv2.imread("Virtual_Decorate/input/decore.jpg")
mask = cv2.imread("Virtual_Decorate/input/mask.jpg")

# resize home to decore shape
home_ = cv2.resize(home, (decore.shape[1], decore.shape[0]))

mask_ = mask.astype("float32")

# set decore on floar
result = mask_ / 255 * decore

# convert mask colors
mask_ = 255 - mask_

# set home appliance on converted mask
result += mask_ / 255 * home_
# change result type
result = result.astype("uint8")

# save image
cv2.imwrite("Virtual_Decorate/output/result.jpg", result)
 