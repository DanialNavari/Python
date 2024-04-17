import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_main_ui import Ui_MainWindow


class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.objects = ["paper", "rock", "scissors"]
        self.cpu = random.choice(self.objects)
        self.ui.cpu.setStyleSheet(
            "background-image: url(:/img/"
            + self.cpu
            + ".png);background-repeat:no-repeat;background-position:center center;"
        )
        self.ui.result.hide()
        self.ui.cpu.hide()
        self.ui.restart.clicked.connect(self.new_game)
        self.ui.paper.clicked.connect(partial(self.player_move, "paper"))
        self.ui.rock.clicked.connect(partial(self.player_move, "rock"))
        self.ui.scissors.clicked.connect(partial(self.player_move, "scissors"))

    def player_move(self, move):
        cpu_score = int(self.ui.cpu_score.text())
        player_score = int(self.ui.player_score.text())
        self.ui.cpu.show()
        self.ui.player.setStyleSheet(
            "background-image: url(:/img/"
            + move
            + ".png);background-repeat:no-repeat;background-position:center center;"
        )
        match self.cpu:
            case "paper":
                if move == "rock":
                    msgbox = "Computer Win!!"
                    cpu_score += 1
                elif move == "scissors":
                    msgbox = "Computer Win!!"
                    cpu_score += 1
                else:
                    msgbox = "Draw..."

            case "rock":
                if move == "paper":
                    msgbox = "Player Win!!"
                    player_score += 1
                elif move == "scissors":
                    msgbox = "Computer Win!!"
                    player_score += 1
                else:
                    msgbox = "Draw..."

            case "scissors":
                if move == "paper":
                    msgbox = "Computer Win!!"
                    cpu_score += 1
                elif move == "rock":
                    msgbox = "Player Win!!"
                    player_score += 1
                else:
                    msgbox = "Draw..."
                    
        
        self.ui.result.setText(msgbox)
        self.ui.result.show()
        self.ui.cpu_score.setText(str(cpu_score))
        self.ui.player_score.setText(str(player_score))

    def new_game(self):
        self.ui.result.hide()
        self.ui.cpu.hide()
        self.ui.player.setStyleSheet("background-image: ''")
        self.cpu = random.choice(self.objects)
        self.ui.cpu.setStyleSheet(
            "background-image: url(:/img/"
            + self.cpu
            + ".png);background-repeat:no-repeat;background-position:center center;"
        )


app = QApplication(sys.argv)
game = Game()
game.show()
app.exec()
