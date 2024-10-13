import cv2

cap = cv2.VideoCapture(0)
_, frame = cap.read()

rows = frame.shape[0]
cols = frame.shape[1]

rect_length = 100
row_mid = int((rows - rect_length) / 2)
col_mid = int((cols - rect_length) / 2)

rect_row_start = row_mid
rect_row_end = row_mid + rect_length

rect_col_start = col_mid
rect_col_end = col_mid + rect_length

while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.rectangle(
        frame, (rect_col_start, rect_row_start), (rect_col_end, rect_row_end), 0, 4
    )
    
    cent_color_code = frame[(rect_col_start + rect_length), (rect_row_start + rect_length)]

    if frame[(rect_col_start + rect_length), (rect_row_start + rect_length)] < 100:
        cv2.putText(frame, f"BLACK({cent_color_code})", (20, 30), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 2)
    elif (
        frame[(rect_col_start + rect_length), (rect_row_start + rect_length)] >= 100
        and frame[(rect_col_start + rect_length), (rect_row_start + rect_length)] <= 140
    ):
        cv2.putText(frame, f"GREY({cent_color_code})", (20, 30), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 2)
    else:
        cv2.putText(frame, f"WHITE({cent_color_code})", (20, 30), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 2)

    cv2.imshow("", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
