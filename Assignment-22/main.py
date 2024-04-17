import sys
from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QWidget
from main_window import Ui_MainWindow
from add_new_task import Ui_MainWindow_task
from database import Database
from functools import partial

class MainAddNewTask(QMainWindow):
    def __init__(self):
        super().__init__()
        self.new_task_ui = Ui_MainWindow_task()
        self.new_task_ui.setupUi(self)
        self.db = Database()
        self.new_task_ui.back_btn.clicked.connect(self.back_page)
        self.new_task_ui.save_btn.clicked.connect(self.save_btn)

    def back_page(self):
        new_task.hide()
        main_window.show()

    def reset(self):
        self.new_task_ui.tb_new_task.setText("")
        self.new_task_ui.tb_new_desc.setText("")
        self.new_task_ui.tb_hafte.setText("")
        self.new_task_ui.tarikh.setText("")
        self.new_task_ui.saat.setText("")

    def save_btn(self):
        onvan = self.new_task_ui.tb_new_task.text()
        sharh = self.new_task_ui.tb_new_desc.toPlainText()
        important = self.new_task_ui.rb_important.isChecked()
        normal = self.new_task_ui.rb_normal.isChecked()
        hafte = self.new_task_ui.tb_hafte.text()
        tarikh = self.new_task_ui.tarikh.text()
        saat = self.new_task_ui.saat.text()

        periority = 0
        time = hafte + " " + tarikh + " ، " + saat
        if important == True:
            periority = 1
        elif normal == True:
            periority = 0
            
        result = self.db.add_new_task(onvan, sharh, time, periority)
        if result == True:
            msgbox = QMessageBox(text="وظیفه جدید با موفقیت ذخیره شد")
            msgbox.exec()
            self.reset()
            new_task.hide()
            main_window.read_from_db()
            main_window.show()
            
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = Database()
        self.read_from_db()
        self.ui.add_new_task_btn.clicked.connect(self.new_task)

    def reset_ui(self):
        layout = self.ui.gl_tasks
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def read_from_db(self):
        self.reset_ui()
        tasks = self.db.get_tasks(-1)

        for i in range(len(tasks)):
            # check button
            new_check_box = QPushButton()
            if tasks[i][3] == 1:
                new_check_box.setStyleSheet('image: url(":/btn/check.png");border:none;')
            else:
                new_check_box.setStyleSheet('image: url(":btn/empty.png");border:none;')

            new_check_box.setMaximumHeight(41)
            new_check_box.setMaximumWidth(41)
            new_check_box.setCursor(Qt.PointingHandCursor)
            new_check_box.setObjectName("c" + str(tasks[i][0]))
            new_check_box.clicked.connect(
                partial(self.check_task, "c" + str(tasks[i][0]))
            )

            # task title
            new_label = QLabel()
            new_label.setText(tasks[i][1])
            new_label.setFont("Yekan Bakh FaNum")
            new_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            if tasks[i][5] == 1:
                colors = "color:red"
            else:
                colors = "color:#000"
            new_label.setStyleSheet("font-size:14px;" + colors)
            new_label.setCursor(Qt.PointingHandCursor)

            # delete buutton
            new_btn = QPushButton()
            new_btn.setObjectName("d" + str(tasks[i][0]))
            new_btn.setMaximumHeight(31)
            new_btn.setMaximumWidth(31)
            new_btn.setStyleSheet('image: url(":/btn/trash.png");border:none;')
            new_btn.setCursor(Qt.PointingHandCursor)
            new_btn.clicked.connect(partial(self.del_task, "c" + str(tasks[i][0])))

            # add widgets to grid layout
            self.ui.gl_tasks.addWidget(new_check_box, i, 0)
            self.ui.gl_tasks.addWidget(new_btn, i, 1)
            self.ui.gl_tasks.addWidget(new_label, i, 2)

            new_label.mousePressEvent = partial(self.get_desc, 'l' + str(tasks[i][0]), i)

    def new_task(self): 
        main_window.hide()
        new_task.show()

    def check_task(self, btn_name):
        result = self.db.task_done(btn_name)
        if result == True:
            self.read_from_db()

    def del_task(self, btn_name):
        msgbox = QMessageBox()
        qq = msgbox.question(self,'', "آیا می خواهید این وظیفه حذف شود؟")
        if qq == 16384:
            self.db.task_delete(btn_name)
            self.read_from_db()

    def get_desc(self, id, row, elses):
        self.reset_ui()
        self.read_from_db()
        tasks = self.db.get_tasks(id)

        # task time
        time_label = QLabel()
        time_label.setText(tasks[0][4])
        time_label.setFont("Yekan Bakh FaNum")
        time_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        if tasks[0][5] == 1:
            colors = "color:red"
        else:
            colors = "color:#000"
        time_label.setStyleSheet("font-size:14px;" + colors)

        # task description
        desc_label = QLabel()
        desc_label.setText(tasks[0][2])
        desc_label.setFont("Yekan Bakh FaNum")
        desc_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        if tasks[0][5] == 1:
            colors = "color:red"
        else:
            colors = "color:#000"
        desc_label.setStyleSheet("font-size:14px;" + colors)

        self.ui.gl_tasks.addWidget(time_label,row,3)
        self.ui.gl_tasks.addWidget(desc_label,row,4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
    main_window.show()
    new_task = MainAddNewTask()
    app.exec()
