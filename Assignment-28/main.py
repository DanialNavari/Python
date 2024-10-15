import cv2

image = cv2.imread("image/dani.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_sticker = cv2.imread("image/sticker.jpg")
image_sticker_gray = cv2.cvtColor(image_sticker, cv2.COLOR_BGR2GRAY)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)
_, frame = cap.read()

while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(frame, 1.3)

    for face in faces:
        x, y, w, h = face
        cv2.rectangle(frame, [x, y], [x + w, y + h], 0, 2)
        image_sticker_gray = cv2.resize(image_sticker_gray, [w, h])
        frame[y : y + h, x : x + w] = image_sticker_gray

    cv2.imshow("", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.imwrite("image/result.jpg", frame)
        break
