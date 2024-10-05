import cv2

profile = cv2.imread("images/profile.png")
profile_cvt = cv2.cvtColor(profile, cv2.COLOR_BGR2GRAY)

start_width_black_tap = 50
black_tap_length = 20

for i in range(70):
    if start_width_black_tap >= 0:
        end_black_tap = start_width_black_tap + black_tap_length
        profile_cvt[i : i + 1, start_width_black_tap:end_black_tap] = 0
        start_width_black_tap -= 1
    else:
        profile_cvt[i : i + 1, 0:black_tap_length] = 0
        black_tap_length -= 1

    cv2.imwrite("images/black_tap.jpg", profile_cvt)
