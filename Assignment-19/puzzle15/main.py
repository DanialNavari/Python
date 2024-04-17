import sys
import random
import time
import datetime
from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from mainwindow_ui import Ui_ui_mainwindow
from scoreboard_ui import Ui_MainWindow
from functools import partial


class ScoreBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scoreboard = Ui_MainWindow()
        self.scoreboard.setupUi(self)
        self.scoreboard.btn_retrn.clicked.connect(self.return_game)

    def return_game(self):
        self.hide()
        main_window.show()

    def add(self, add_num, type="move"):
        if type == "score":
            yekan = int(self.scoreboard.s1.text())
            dahgan = int(self.scoreboard.s2.text()) * 10
            sadgan = int(self.scoreboard.s3.text()) * 100
            hezargan = int(self.scoreboard.s4.text()) * 1000

            total = yekan + dahgan + sadgan + hezargan + add_num
            if total == 0:
                jam = "0000"
            if total > 0 and total < 10:
                jam = "000" + str(total)
            if total >= 10 and total < 100:
                jam = "00" + str(total)
            if total >= 100 and total < 1000:
                jam = "0" + str(total)

            self.scoreboard.s1.setText(jam[3])
            self.scoreboard.s2.setText(jam[2])
            self.scoreboard.s3.setText(jam[1])
            self.scoreboard.s4.setText(jam[0])

        elif type == "move":
            yekan_m = int(self.scoreboard.m1.text())
            dahgan_m = int(self.scoreboard.m2.text()) * 10
            sadgan_m = int(self.scoreboard.m3.text()) * 100
            hezargan_m = int(self.scoreboard.m4.text()) * 1000

            total_m = yekan_m + dahgan_m + sadgan_m + hezargan_m + add_num
            if total_m == 0:
                jam_m = "0000"
            if total_m > 0 and total_m < 10:
                jam_m = "000" + str(total_m)
            if total_m >= 10 and total_m < 100:
                jam_m = "00" + str(total_m)
            if total_m >= 100 and total_m < 1000:
                jam_m = "0" + str(total_m)

            self.scoreboard.m1.setText(jam_m[3])
            self.scoreboard.m2.setText(jam_m[2])
            self.scoreboard.m3.setText(jam_m[1])
            self.scoreboard.m4.setText(jam_m[0])

    def elapsed(self,value):
        tabdil = str(datetime.timedelta(seconds=int(value)))
        tabdil_ = tabdil.split(":")
        minute = tabdil_[1]
        seconds = tabdil_[2]
        self.scoreboard.hh.setText(minute[0])
        self.scoreboard.h.setText(minute[1])

        self.scoreboard.mm.setText(seconds[0])
        self.scoreboard.m.setText(seconds[1])


class GamePlay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.start = time.time()

        self.ui = Ui_ui_mainwindow()
        self.ui.setupUi(self)

        self.araye = []

        self.buttons = [
            [self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4],
            [self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btbn_8],
            [self.ui.btn_9, self.ui.btn_10, self.ui.btn_11, self.ui.btn_12],
            [self.ui.btn_13, self.ui.btn_14, self.ui.btn_15, self.ui.btn_16],
        ]

        for i in range(4):
            for j in range(4):
                r = random.randint(1, 16)
                while r in self.araye:
                    r = random.randint(1, 16)
                else:
                    self.buttons[i][j].setText(str(r))
                    self.buttons[i][j].clicked.connect(partial(self.play, i, j))
                    self.araye.append(r)
                if r == 16:
                    self.empty_i = i
                    self.empty_j = j
                    self.buttons[i][j].hide()
        self.ui.score.clicked.connect(self.show_score)

    def show_score(self):
        self.end = time.time()
        score_board.elapsed(str(int(self.end - self.start)))
        self.hide()
        score_board.show()

    def play(self, i, j):
        score_board.add(1, "move")
        if (i == self.empty_i and abs(j - self.empty_j) == 1) or (
            j == self.empty_j and abs(i - self.empty_i) == 1
        ):
            self.buttons[self.empty_i][self.empty_j].setText(self.buttons[i][j].text())
            self.buttons[i][j].setText("16")
            self.buttons[self.empty_i][self.empty_j].show()
            self.buttons[i][j].hide()
            self.empty_i = i
            self.empty_j = j
        if self.check_win() == True:
            msgbox = QMessageBox()
            msgbox.setText("شما برنده شدید🎁")
            msgbox.exec()

    def check_win(self):
        index = 1
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text()) != index:
                    index += 1
                    return False
        return True


app = QApplication(sys.argv)

main_window = GamePlay()
score_board = ScoreBoard()

main_window.show()


app.exec()
