import cv2

chess_board = cv2.imread("images/bg.jpg")
chess_board_cvt = cv2.cvtColor(chess_board, cv2.COLOR_BGR2GRAY)

black_step = 50

for i in range(0, 8):
    for j in range(0, 8):
        if i % 2 == 0 and j % 2 != 0:
            color = 0

        elif i % 2 != 0 and j % 2 == 0:
            color = 0

        else:
            color = 255

        # set col home position
        col_start_black = j * black_step
        col_end_black = col_start_black + black_step

        # set row home position
        row_start_black = i * black_step
        row_end_black = row_start_black + black_step

        # set home position color
        chess_board_cvt[
            row_start_black:row_end_black, col_start_black:col_end_black
        ] = color

        # save image
        cv2.imwrite("images/result.jpg", chess_board_cvt)
