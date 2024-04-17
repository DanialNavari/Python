# import libraries
import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

# variables
player = 1
move = 0
btn_list = []


# define functions
def show_winner(game_board, symbol):
    global move
    winner = ""

    if winner == "":
        col1 = (
            game_board[0][0].text() + game_board[1][0].text() + game_board[2][0].text()
        )
        col2 = (
            game_board[0][1].text() + game_board[1][1].text() + game_board[2][1].text()
        )
        col3 = (
            game_board[0][2].text() + game_board[1][2].text() + game_board[2][2].text()
        )
        col4 = (
            game_board[0][0].text() + game_board[1][1].text() + game_board[2][2].text()
        )
        col5 = (
            game_board[0][2].text() + game_board[1][1].text() + game_board[2][0].text()
        )
        col6 = (
            game_board[0][0].text() + game_board[0][1].text() + game_board[0][2].text()
        )
        col7 = (
            game_board[1][0].text() + game_board[1][1].text() + game_board[1][2].text()
        )
        col8 = (
            game_board[2][0].text() + game_board[2][1].text() + game_board[2][2].text()
        )

        if (
            col1 == symbol * 3
            or col2 == symbol * 3
            or col3 == symbol * 3
            or col4 == symbol * 3
            or col5 == symbol * 3
            or col6 == symbol * 3
            or col7 == symbol * 3
            or col8 == symbol * 3
        ):
            winner = symbol

            for row in range(3):
                for col in range(3):
                    button[row][col].setText(buttons[row][col].text())
                    button[row][col].setStyleSheet("border:none")
                    button[row][col].setStyleSheet("color:silver")

            if col1 == symbol * 3:
                win.btn_1.setStyleSheet("color:orange")
                win.btn_4.setStyleSheet("color:orange")
                win.btn_7.setStyleSheet("color:orange")
            if col2 == symbol * 3:
                win.btn_2.setStyleSheet("color:orange")
                win.btn_5.setStyleSheet("color:orange")
                win.btn_8.setStyleSheet("color:orange")
            if col3 == symbol * 3:
                win.btn_3.setStyleSheet("color:orange")
                win.btn_6.setStyleSheet("color:orange")
                win.btn_9.setStyleSheet("color:orange")
            if col4 == symbol * 3:
                win.btn_1.setStyleSheet("color:orange")
                win.btn_5.setStyleSheet("color:orange")
                win.btn_9.setStyleSheet("color:orange")
            if col5 == symbol * 3:
                win.btn_3.setStyleSheet("color:orange")
                win.btn_5.setStyleSheet("color:orange")
                win.btn_7.setStyleSheet("color:orange")
            if col6 == symbol * 3:
                win.btn_1.setStyleSheet("color:orange")
                win.btn_2.setStyleSheet("color:orange")
                win.btn_3.setStyleSheet("color:orange")
            if col7 == symbol * 3:
                win.btn_4.setStyleSheet("color:orange")
                win.btn_5.setStyleSheet("color:orange")
                win.btn_6.setStyleSheet("color:orange")
            if col8 == symbol * 3:
                win.btn_7.setStyleSheet("color:orange")
                win.btn_8.setStyleSheet("color:orange")
                win.btn_9.setStyleSheet("color:orange")

        elif move == 9 and winner == "":
            winner = "XO"

    return winner

def reset_game(game_board):
    global move, player, btn_list
    move = 0
    window.mov.setText("0")
    window.same.setText("0")
    for i in range(3):
        for j in range(3):
            game_board[i][j].setText("")
            game_board[i][j].setStyleSheet("background: #cacaca;color:transparent")
    window.xsign.setStyleSheet("image: url(X.png);")
    window.osign.setStyleSheet("image: url(o1.png);")
    player = 1
    btn_list = []

def clear_data():
    reset_game(buttons)
    window.Oscore.setText("0")
    window.Xscore.setText("0")

def num_to_i_j(num):
    global ij
    ij = []

    if num == 1:
        ij = [0, 0]
    if num == 2:
        ij = [0, 1]
    if num == 3:
        ij = [0, 2]
    if num == 4:
        ij = [1, 0]
    if num == 5:
        ij = [1, 1]
    if num == 6:
        ij = [1, 2]
    if num == 7:
        ij = [2, 0]
    if num == 8:
        ij = [2, 1]
    if num == 9:
        ij = [2, 2]

    return ij

def i_j_to_num(i, j):
    global btn_list
    if i == 0 and j == 0:
        btn_list.append(1)
    if i == 0 and j == 1:
        btn_list.append(2)
    if i == 0 and j == 2:
        btn_list.append(3)
    if i == 1 and j == 0:
        btn_list.append(4)
    if i == 1 and j == 1:
        btn_list.append(5)
    if i == 1 and j == 2:
        btn_list.append(6)
    if i == 2 and j == 0:
        btn_list.append(7)
    if i == 2 and j == 1:
        btn_list.append(8)
    if i == 2 and j == 2:
        btn_list.append(9)

def play(i, j, mode):
    global player, move, btn_list

    window.vs.setText(mode) 
    if mode == "vsplayer":
        if player == 1:
            buttons[i][j].setStyleSheet(
                "background: #cacaca url(X1.png) center center no-repeat;color:transparent"
            )
            window.xsign.setStyleSheet("image: url(x1.png);")
            window.osign.setStyleSheet("image: url(O.png);")
            buttons[i][j].setText("X")
            w = show_winner(buttons, "X")
            if w == "X":
                win.result.setText("برنده : بازیکن 1")
                win.show()
                window.hide()
                xscore = int(window.Xscore.text())
                xscore += 1
                window.Xscore.setText(str(xscore))
                reset_game(buttons)
                player = 1
            elif move == 8 and w == "XO":
                q = QMessageBox(text="مساوی")
                q.show()
                q.exec()
                reset_game(buttons)
                sam = int(window.same.text())
                sam +=1
                window.same.setText(str(sam))
                player = 1
            else:
                player = 2
        elif player == 2:
            buttons[i][j].setStyleSheet(
                "background: #cacaca url(O1.png) center center no-repeat;color:transparent"
            )
            window.xsign.setStyleSheet("image: url(X.png);")
            window.osign.setStyleSheet("image: url(o1.png);")
            buttons[i][j].setText("O")
            w = show_winner(buttons, "O")
            if w == "O":
                win.result.setText("برنده : بازیکن 2")
                win.show()
                window.hide()
                oscore = int(window.Oscore.text())
                oscore += 1
                window.Oscore.setText(str(oscore))
                reset_game(buttons)
                player = 2
            elif move == 9 and w == "XO":
                q = QMessageBox(text="مساوی")
                q.show()
                q.exec()
                reset_game(buttons)
                sam = int(window.same.text())
                sam +=1
                window.same.setText(str(sam))
            else:
                player = 1
    elif mode == "vscomputer":
        i_j_to_num(i, j)

        if player == 1:
            buttons[i][j].setStyleSheet(
                "background: #cacaca url(X1.png) center center no-repeat;color:transparent"
            )
            window.xsign.setStyleSheet("image: url(x1.png);")
            window.osign.setStyleSheet("image: url(O.png);")
            buttons[i][j].setText("X")
            w = show_winner(buttons, "X")
            if w == "X":
                win.result.setText("برنده : بازیکن 1")
                win.show()
                window.hide()
                xscore = int(window.Xscore.text())
                xscore += 1
                window.Xscore.setText(str(xscore))
                reset_game(buttons)
                player = 1
            elif move == 8 and w == "XO":
                q = QMessageBox(text="مساوی")
                q.show()
                q.exec()
                sam = int(window.same.text())
                sam +=1
                window.same.setText(str(sam))
                reset_game(buttons)
            player = 2
        elif player == 2:
            rnd = random.randint(1, 9)
            while rnd in btn_list:
                rnd = random.randint(1, 9)
            btn_list.append(rnd)
            i_j = num_to_i_j(rnd)

            buttons[i_j[0]][i_j[1]].setStyleSheet(
                "background: #cacaca url(O1.png) center center no-repeat;color:transparent"
            )
            window.xsign.setStyleSheet("image: url(X.png);")
            window.osign.setStyleSheet("image: url(o1.png);")
            buttons[i_j[0]][i_j[1]].setText("O")

            w = show_winner(buttons, "O")
            if w == "O":
                win.result.setText("برنده : کامپیوتر")
                win.show()
                window.hide()
                oscore = int(window.Oscore.text())
                oscore += 1
                window.Oscore.setText(str(oscore))
                reset_game(buttons)
                player = 2
            elif move == 9 and w == "XO":
                q = QMessageBox(text="مساوی")
                q.show()
                q.exec()
                sam = int(window.same.text())
                sam +=1
                window.same.setText(str(sam))
                reset_game(buttons)
            player = 1
    move +=1
    window.mov.setText(str(move))

def return_game():
    win.hide()
    window.show()
    reset_game(buttons)
    for i in range(3):
        for j in range(3):
            button[i][j].setStyleSheet("color:silver")

def mode(mode):
    clear_data()
    for k in range(3):
        for l in range(3):
            buttons[k][l].clicked.connect(partial(play, k, l, mode))

def about():
    a = QMessageBox(text=".::بازی تیک تاک تو::.\nاین بازی توسط دانیال نواری جهت تمرین شماره 18 طراحی شده است")
    a.show()
    a.exec()

# app & loader & ui
loader = QUiLoader()
app = QApplication([])
window = loader.load("ui.ui")
win = loader.load("winner.ui")

# buttons
buttons = [
    [
        window.btn_1,
        window.btn_2,
        window.btn_3,
    ],
    [
        window.btn_4,
        window.btn_5,
        window.btn_6,
    ],
    [
        window.btn_7,
        window.btn_8,
        window.btn_9,
    ],
]

button = [
    [
        win.btn_1,
        win.btn_2,
        win.btn_3,
    ],
    [
        win.btn_4,
        win.btn_5,
        win.btn_6,
    ],
    [
        win.btn_7,
        win.btn_8,
        win.btn_9,
    ],
]

# connect bottuns to functions
win.new_game.clicked.connect(return_game)
window.about.clicked.connect(about)
window.restart.clicked.connect(clear_data)
window.vscomputer.clicked.connect(partial(mode, mode="vscomputer"))
window.vsplayer.clicked.connect(partial(mode, mode="vsplayer"))
window.vsplayer.click()

window.vs.hide()
window.mov.hide()

window.show()
app.exec()
