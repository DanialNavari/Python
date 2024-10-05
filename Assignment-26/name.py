import cv2

bg = cv2.imread("images/bg.jpg")
bg_cvt = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)

bg_cvt[100:200, 100:110] = 0
bg_cvt[100:110, 110:140] = 0
bg_cvt[110:120, 140:150] = 0
bg_cvt[120:130, 150:160] = 0
bg_cvt[130:140, 160:170] = 0
bg_cvt[140:150, 170:180] = 0
bg_cvt[150:160, 170:180] = 0
bg_cvt[160:170, 160:170] = 0
bg_cvt[170:180, 150:160] = 0
bg_cvt[180:190, 140:150] = 0
bg_cvt[190:200, 100:140] = 0
cv2.imwrite("name.jpg", bg_cvt)
