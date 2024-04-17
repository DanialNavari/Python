# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QWidget)
import bg_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(796, 491)
        font = QFont()
        font.setFamilies([u"Yekan Bakh FaNum"])
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setStyleSheet(u"")
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.add_new_task_btn = QPushButton(self.centralwidget)
        self.add_new_task_btn.setObjectName(u"add_new_task_btn")
        self.add_new_task_btn.setGeometry(QRect(360, 420, 81, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_new_task_btn.sizePolicy().hasHeightForWidth())
        self.add_new_task_btn.setSizePolicy(sizePolicy)
        self.add_new_task_btn.setMinimumSize(QSize(0, 30))
        self.add_new_task_btn.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.add_new_task_btn.setFont(font1)
        self.add_new_task_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_new_task_btn.setStyleSheet(u"border:none;\n"
"image: url(:/btn/plus.png);\n"
"")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 25, 781, 391))
        self.gl_tasks = QGridLayout(self.layoutWidget)
        self.gl_tasks.setObjectName(u"gl_tasks")
        self.gl_tasks.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_new_task_btn.setText("")
    # retranslateUi

