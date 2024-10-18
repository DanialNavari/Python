# import library
import cv2

# Reading image and convert it's color mode to gray
cat_image = cv2.imread("cat_face_detection/image/cats.jpg")
cat_image_gray = cv2.cvtColor(cat_image, cv2.COLOR_BGR2GRAY)

# Create face detector
cat_face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalcatface.xml"
)

# Detect cat face
cat_faces = cat_face_detector.detectMultiScale(cat_image_gray, 1.1, 1)

# Draw a rectangle around cats' face
for cat_face in cat_faces:
    x, y, w, h = cat_face
    cv2.rectangle(cat_image, [x, y], [x + w, y + h], [255, 255, 255], 1)

# Print number of cats
cat_count = cat_faces.__len__()
cv2.putText(cat_image, f"Count: {cat_count}", [20, 40], cv2.FONT_HERSHEY_TRIPLEX, 1, 0)

# Show image
cv2.imshow("", cat_image)
cv2.waitKey()
