import sys
from database import Database
from PySide6.QtCore import QObject, QThread, Signal, Qt
from PySide6.QtWidgets import *
from functools import partial
from add_alarm_window import Addalarm


class Winalarm(QThread):
    signal_alarm = Signal(str)

    def __init__(self, ui):
        super().__init__()
        self.database = Database()
        self.alarm_list = self.database.get_alarm()
        self.ui = ui
        self.layout = self.ui.alarm_box

    def run(): ...

    def reset_ui(self):
        for i in reversed(range(self.layout.count())):
            item = self.layout.itemAt(i)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def show_alarm(self):
        # self.reset_ui()
        for i in range(len(self.alarm_list)):
            new_label = QLabel()
            new_label.setText(self.alarm_list[i][1])
            new_label.setFont("IRANYekanX Bold")
            new_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            new_label.setStyleSheet("font-size:14px;")

            new_label_ = QLabel()
            new_label_.setText(
                str(self.alarm_list[i][2]) + ":" + str(self.alarm_list[i][3])
            )
            new_label_.setFont("IRANYekanX Bold")
            new_label_.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            new_label_.setStyleSheet("font-size:14px;")

            # delete buutton
            new_btn = QPushButton()
            new_btn.setObjectName("d" + str(self.alarm_list[i][0]))
            new_btn.setMaximumHeight(31)
            new_btn.setMaximumWidth(31)
            new_btn.setStyleSheet("image: url(:/flag/trash.png);")
            new_btn.setCursor(Qt.PointingHandCursor)
            new_btn.clicked.connect(
                partial(self.del_task, "c" + str(self.alarm_list[i][0]))
            )

            self.layout.addWidget(new_btn, i, 0)
            self.layout.addWidget(new_label, i, 1)
            self.layout.addWidget(new_label_, i, 2)

    def add_alarm(self):
        self.ui.hide()

    def del_task(self, btn_name):
        msgbox = QMessageBox()
        qq = msgbox.question(self, "", "آیا می خواهید این هشدار حذف شود؟")
        if qq == 16384:
            self.database.del_alarm(btn_name)
            self.show_alarm()



