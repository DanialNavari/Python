# import libraries
import cv2

# Read football empty pitch
football_pitch = cv2.imread("image/football.jpg")

# Draw area of pitch and gates place
cv2.rectangle(football_pitch, [20, 20], [592, 439], [255, 255, 255], 2)
cv2.line(football_pitch, [306, 20], [306, 439], [255, 255, 255], 2)
cv2.rectangle(football_pitch, [20, 120], [120, 330], [255, 255, 255], 2)
cv2.rectangle(football_pitch, [20, 170], [70, 280], [255, 255, 255], 2)
cv2.rectangle(football_pitch, [492, 120], [592,330], [255, 255, 255], 2)
cv2.rectangle(football_pitch, [542, 170], [592, 280], [255, 255, 255], 2)

# Draw center of football pitch
cv2.circle(football_pitch, [306, 220], 80, [255, 255, 255], 2)
cv2.circle(football_pitch, [306, 220], 4, [255, 255, 255], 5)


# Show football pitch
cv2.imshow("", football_pitch)
cv2.waitKey()
