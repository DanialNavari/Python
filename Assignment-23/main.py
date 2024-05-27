import sys
import random
from sudoku import Sudoku
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_ui import Ui_MainWindow
from winner_ui import Ui_Winner


class WinnerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.winner_ui = Ui_Winner()
        self.winner_ui.setupUi(self)
        self.winner_ui.restart_btn.clicked.connect(self.restart_game)

    def restart_game(self):
        window.new_game()
        window.show()
        winner_form.hide()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_new.triggered.connect(self.new_game)
        self.ui.menu_open.triggered.connect(self.open_file)
        self.ui.actionVery_Easy.triggered.connect(partial(self.set_level, 0.1))
        self.ui.actionEasy.triggered.connect(partial(self.set_level, 0.3))
        self.ui.actionNormal.triggered.connect(partial(self.set_level, 0.5))
        self.ui.actionHard.triggered.connect(partial(self.set_level, 0.7))
        self.ui.actionVery_Hard.triggered.connect(partial(self.set_level, 0.9))
        self.new_game()
        self.answer = True

    def validation(self, i, j, text):
        self.reset_to_defult()
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.line_edits[i][j].setText("")
        if text != None and text != "":
            self.check(i, j)
            self.check_win()

    def new_game(self, lvl=0.5):
        puzzle = Sudoku(3, seed=random.randint(1, 1000)).difficulty(lvl)
        self.line_edits = [[None for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                new_cell.setReadOnly(False)
                if puzzle.board[i][j] != None:
                    new_cell.setText(str(puzzle.board[i][j]))
                    new_cell.setReadOnly(True)

                new_cell.setFixedWidth(50)
                new_cell.setFixedHeight(50)
                new_cell.setAlignment(Qt.AlignVCenter)
                new_cell.setAlignment(Qt.AlignHCenter)
                new_cell.setStyleSheet(
                    "font-size:25px;font-weight:bold;border-radius:5px"
                )
                self.ui.grid_layout.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self, "Open file... ")
        f = open(file_path[0], "r")
        big_text = f.read()
        rows = big_text.split("\n")
        puzzle_board = [[None for i in range(9)] for j in range(9)]

        for i in range(len(rows)):
            cells = rows[i].split(" ")
            for j in range(len(cells)):
                puzzle_board[i][j] = int(cells[j])

        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                new_cell.setReadOnly(False)
                if puzzle_board[i][j] != 0:
                    new_cell.setText(str(puzzle_board[i][j]))
                    new_cell.setReadOnly(True)
                new_cell.setFixedWidth(50)
                new_cell.setFixedHeight(50)
                new_cell.setAlignment(Qt.AlignVCenter)
                new_cell.setAlignment(Qt.AlignHCenter)
                new_cell.setStyleSheet(
                    "font-size:25px;font-weight:bold;border-radius:5px"
                )
                self.ui.grid_layout.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell

    def check(self, i, j):
        user_number = self.line_edits[i][j].text()
        # check row
        for jj in range(0, 9):
            if j != jj:
                col_num = self.line_edits[i][jj].text()
                if col_num == user_number:
                    self.line_edits[i][jj].setStyleSheet(
                        "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffaaff;color:#000"
                    )
                    self.answer = False
                else:
                    self.answer = True

        # check col
        for ii in range(0, 9):
            if i != ii:
                row_num = self.line_edits[ii][j].text()
                if row_num == user_number:
                    self.line_edits[ii][j].setStyleSheet(
                        "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffaaff;color:#000"
                    )
                    self.answer = False
                else:
                    self.answer = True

        # check square
        self.check_all_squares(i, j, user_number)

    def check_all_squares(self, ii, jj, user_number):
        answer = True
        # first three row
        # 1st square
        if ii >= 0 and ii < 3 and jj >= 0 and jj < 3:
            for i in range(0, 3):
                for j in range(0, 3):
                    row_num = self.line_edits[i][j].text()
                    if i != ii and j != jj and row_num == user_number:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffaaff;color:#000"
                        )
                        answer = False
                    else:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffffff;color:#000"
                        )
                        answer = True

        # 2nd square
        if ii >= 0 and ii < 3 and jj >= 3 and jj < 6:
            for i in range(0, 3):
                for j in range(3, 6):
                    row_num = self.line_edits[i][j].text()
                    if i != ii and j != jj and row_num == user_number:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffaaff;color:#000"
                        )
                        answer = False
                    else:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffffff;color:#000"
                        )
                        answer = True

        # 3rd square
        if ii >= 0 and ii < 3 and jj >= 6 and jj < 9:
            for i in range(0, 3):
                for j in range(6, 9):
                    row_num = self.line_edits[i][j].text()
                    if i != ii and j != jj and row_num == user_number:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffaaff;color:#000"
                        )
                        answer = False
                    else:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffffff;color:#000"
                        )
                        answer = True

        # -------------------------------------------------------------------
        # second three row
        # 1st square
        if ii >= 3 and ii < 6 and jj >= 0 and jj < 3:
            for i in range(3, 6):
                for j in range(0, 3):
                    row_num = self.line_edits[i][j].text()
                    if i != ii and j != jj and row_num == user_number:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffaaff;color:#000"
                        )
                        answer = False
                    else:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffffff;color:#000"
                        )
                        answer = True

        # 2nd square
        if ii >= 3 and ii < 6 and jj >= 3 and jj < 6:
            for i in range(3, 6):
                for j in range(3, 6):
                    row_num = self.line_edits[i][j].text()
                    if i != ii and j != jj and row_num == user_number:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffaaff;color:#000"
                        )
                        answer = False
                    else:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffffff;color:#000"
                        )
                        answer = True

        # 3rd square
        if ii >= 3 and ii < 6 and jj >= 6 and jj < 9:
            for i in range(3, 6):
                for j in range(6, 9):
                    row_num = self.line_edits[i][j].text()
                    if i != ii and j != jj and row_num == user_number:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffaaff;color:#000"
                        )
                        answer = False
                    else:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffffff;color:#000"
                        )
                        answer = True

        # -------------------------------------------------------------------
        # third three row
        # 1st square
        if ii >= 6 and ii < 9 and jj >= 0 and jj < 3:
            for i in range(6, 9):
                for j in range(0, 3):
                    row_num = self.line_edits[i][j].text()
                    if i != ii and j != jj and row_num == user_number:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffaaff;color:#000"
                        )
                        answer = False
                    else:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffffff;color:#000"
                        )
                        answer = True

        # 2nd square
        if ii >= 6 and ii < 9 and jj >= 3 and jj < 6:
            for i in range(6, 9):
                for j in range(3, 6):
                    row_num = self.line_edits[i][j].text()
                    if i != ii and j != jj and row_num == user_number:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffaaff;color:#000"
                        )
                        answer = False
                    else:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffffff;color:#000"
                        )
                        answer = True

        # 3rd square
        if ii >= 6 and ii < 9 and jj >= 6 and jj < 9:
            for i in range(6, 9):
                for j in range(6, 9):
                    row_num = self.line_edits[i][j].text()
                    if i != ii and j != jj and row_num == user_number:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffaaff;color:#000"
                        )
                        answer = False
                    else:
                        self.line_edits[i][j].setStyleSheet(
                            "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffffff;color:#000"
                        )
                        answer = True

        self.answer = answer

    def reset_to_defult(self):
        for i in range(0, 9):
            for j in range(0, 9):
                self.line_edits[i][j].setStyleSheet(
                    "font-size:25px;font-weight:bold;border-radius:5px;background-color:#ffffff;color:#000"
                )

    def check_win(self):
        pos = 0
        for i in range(0, 9):
            for j in range(0, 9):
                txt = self.line_edits[i][j].text()
                if txt == None or txt == "":
                    pos += 1

        if pos == 0 and self.answer == True:
            window.hide()
            winner_form.show()

    def set_level(self, level):
        self.new_game(level)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    winner_form = WinnerWindow()
    window.show()
    app.exec()
