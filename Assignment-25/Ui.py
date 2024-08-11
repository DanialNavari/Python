from PySide6.QtWidgets import *
from main_window import Ui_MainWindow


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lbl_stopwatch.setText("0:0:0")
