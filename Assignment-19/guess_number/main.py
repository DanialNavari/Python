import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from converter.main_ui import Ui_MainWindow


class GuessWord(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.num = random.randint(1, 99)
        self.ui.btn_check.clicked.connect(self.check_num)
        
    def check_num(self):
        guess_num = int(self.ui.word.value())
        if guess_num == self.num :
            a = QMessageBox(text="🎉🎉🎉 درست حدس زدی 🎉🎉🎉")
            self.num = random.randint(1, 99)
            self.ui.word.setValue(0)
        elif guess_num > self.num:
            a = QMessageBox(text="🤦‍♂️ برو پایین")
        elif guess_num <self.num:
            a = QMessageBox(text="🤦‍♂️ برو بالا")
        a.show()
        a.exec()

app = QApplication(sys.argv)
gn = GuessWord()
gn.show()
app.exec()