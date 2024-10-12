import cv2
import numpy

cap = cv2.VideoCapture(0)
_, frame = cap.read()
rows = frame.shape[0]
cols = frame.shape[1]

writer = cv2.VideoWriter(
    "my_webcam.avi", cv2.VideoWriter_fourcc(*'H264'), 10, (cols, rows)
)

while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # _, frame = cv2.threshold(frame, 100, 500, cv2.THRESH_BINARY)
    writer.write(frame)
    cv2.imshow("", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

writer.release()
