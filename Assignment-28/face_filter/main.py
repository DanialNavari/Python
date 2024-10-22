# Import libraries
import cv2
import cv2.data
import numpy as np

# Load filter
lion_sticker = cv2.imread("face_filter/input/spiderman.png")
lip_sticker = cv2.imread("face_filter/input/lip.png")
eye_sticker = cv2.imread("face_filter/input/sunglasses.png")

# Filter state
face_mask = False
lip_mask = False
chess_mask = False
mirror_mask = False
eye_mask = False

# Classifiers
global face_detector, lip_detector, eye_detector
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
lip_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")


# Change filter states
def change_filter(active_filter):
    global face_mask, lip_mask, chess_mask, mirror_mask, eye_mask
    face_mask = False
    lip_mask = False
    chess_mask = False
    mirror_mask = False
    eye_mask = False

    match active_filter:
        case "face_mask":
            face_mask = True
        case "eye_mask":
            eye_mask = True
        case "lip_mask":
            lip_mask = True
        case "chess_mask":
            chess_mask = True
        case "mirror_mask":
            mirror_mask = True


# Fit stickers to filter area
def overlay_sticker(frame, sticker, x, y, w, h):
    sticker_resized = cv2.resize(sticker, (w, h))
    sticker_gray = cv2.cvtColor(sticker_resized, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(sticker_gray, 240, 255, cv2.THRESH_BINARY_INV)
    mask_inv = cv2.bitwise_not(mask)

    face_area = frame[y : y + h, x : x + w]
    fg = cv2.bitwise_and(sticker_resized, sticker_resized, mask=mask)
    bg = cv2.bitwise_and(face_area, face_area, mask=mask_inv)
    frame[y : y + h, x : x + w] = cv2.add(fg, bg)


# Manage all filter
def filter_face(frame, object):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray, scaleFactor=1.3)

    for face in faces:
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        x, y, w, h = face

        if object == "eye":
            eyes = eye_detector.detectMultiScale(
                frame_gray[y : y + h, x : x + w], scaleFactor=1.1, minNeighbors=5
            )
            for eye in eyes:
                if len(eye) > 1:
                    sorted_eyes = sorted(eyes, key=lambda e: e[0])
                    if len(sorted_eyes) >= 2:
                        left_eye = sorted_eyes[0]
                        right_eye = sorted_eyes[1]

                        glasses_width = right_eye[0] + right_eye[2] - left_eye[0]
                        glasses_height = max(left_eye[3], right_eye[3])
                        glasses_x = x + left_eye[0]
                        glasses_y = y + min(left_eye[1], right_eye[1])

                        overlay_sticker(
                            frame,
                            eye_sticker,
                            glasses_x,
                            glasses_y,
                            glasses_width,
                            glasses_height,
                        )
        elif object == "lip":
            smiles = lip_detector.detectMultiScale(
                frame_gray[y : y + h, x : x + w],
                scaleFactor=1.7,
                minNeighbors=22,
                minSize=(25, 25),
            )
            for smile in smiles:
                if len(smile) > 0:
                    xxx = x + smile[0]
                    yyy = y + smile[1]
                    www = smile[2]
                    hhh = smile[3]
                    overlay_sticker(frame, lip_sticker, xxx, yyy, www, hhh)
        elif object == "face":
            faces = face_detector.detectMultiScale(frame_gray, 1.3, 4)
            for face in faces:
                x, y, w, h = face
                overlay_sticker(frame, lion_sticker, x, y, w, h)
        elif object == "chess":
            small_pixel_square = cv2.resize(frame_gray[y : y + h, x : x + w], [20, 20])
            large_pixel_square = cv2.resize(
                small_pixel_square, [w, h], interpolation=cv2.INTER_NEAREST
            )
            face_image_big_bgr = cv2.cvtColor(large_pixel_square, cv2.COLOR_GRAY2BGR)
            frame[y : y + h, x : x + w] = face_image_big_bgr
        elif object == "mirror":
            center_x = frame.shape[1] // 2
            left_side = frame[:, :center_x]
            right_side = frame[:, center_x:]
            mirrored_left_side = cv2.flip(left_side, 1)
            combined_image = np.hstack((left_side, mirrored_left_side))
            frame[:,:] = combined_image


# Read from webcam
cap = cv2.VideoCapture(0)
_, frame = cap.read()


while True:
    _, frame = cap.read()

    if _ != True:
        break
    else:

        key = cv2.waitKey(1) & 0xFF

        # Check filter activate condition
        if face_mask:
            filter_face(frame, "face")
        elif lip_mask:
            filter_face(frame, "lip")
        elif eye_mask:
            filter_face(frame, "eye")
        elif chess_mask:
            filter_face(frame, "chess")
        elif mirror_mask:
            filter_face(frame, "mirror")

        # Show image
        cv2.imshow("result", frame)

        # Check key press
        if key == ord("1"):
            change_filter("face_mask")
            cv2.imwrite("face_filter/output/face_mask.jpg", frame)
        elif key == ord("2"):
            change_filter("eye_mask")
            cv2.imwrite("face_filter/output/eye_mask.jpg", frame)
        elif key == ord("3"):
            change_filter("lip_mask")
            cv2.imwrite("face_filter/output/lip_mask.jpg", frame)
        elif key == ord("4"):
            change_filter("chess_mask")
            cv2.imwrite("face_filter/output/chess_mask.jpg", frame)
        elif key == ord("5"):
            change_filter("mirror_mask")
            cv2.imwrite("face_filter/output/mirror_mask.jpg", frame)
        elif key == ord("q"):
            break
