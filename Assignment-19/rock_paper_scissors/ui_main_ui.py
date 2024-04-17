# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(252, 455)
        MainWindow.setMinimumSize(QSize(252, 455))
        MainWindow.setMaximumSize(QSize(252, 455))
        MainWindow.setStyleSheet(u"background-color: rgb(164, 209, 31);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.rock = QPushButton(self.centralwidget)
        self.rock.setObjectName(u"rock")
        self.rock.setGeometry(QRect(10, 320, 75, 61))
        self.rock.setStyleSheet(u"background-image: url(:/img/rock.png);\n"
"background-position:center center;")
        self.paper = QPushButton(self.centralwidget)
        self.paper.setObjectName(u"paper")
        self.paper.setGeometry(QRect(90, 320, 75, 61))
        self.paper.setStyleSheet(u"background-image: url(:/img/paper.png);\n"
"background-position:center center;")
        self.scissors = QPushButton(self.centralwidget)
        self.scissors.setObjectName(u"scissors")
        self.scissors.setGeometry(QRect(170, 320, 75, 61))
        self.scissors.setStyleSheet(u"background-image: url(:/img/scissors.png);\n"
"background-position:center center;")
        self.cpu_box = QLabel(self.centralwidget)
        self.cpu_box.setObjectName(u"cpu_box")
        self.cpu_box.setGeometry(QRect(90, 60, 91, 91))
        self.cpu_box.setStyleSheet(u"border:2px dashed rgb(74,125,0);\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 0, 91, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(68, 68, 68);")
        self.label.setAlignment(Qt.AlignCenter)
        self.player_box = QLabel(self.centralwidget)
        self.player_box.setObjectName(u"player_box")
        self.player_box.setGeometry(QRect(90, 160, 91, 91))
        self.player_box.setStyleSheet(u"border:2px dashed rgb(74,125,0);\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 290, 91, 31))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(68, 68, 68);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.cpu_score = QLabel(self.centralwidget)
        self.cpu_score.setObjectName(u"cpu_score")
        self.cpu_score.setGeometry(QRect(90, 30, 91, 31))
        font1 = QFont()
        font1.setPointSize(19)
        font1.setBold(True)
        self.cpu_score.setFont(font1)
        self.cpu_score.setStyleSheet(u"color: rgb(255, 14, 58);")
        self.cpu_score.setAlignment(Qt.AlignCenter)
        self.player_score = QLabel(self.centralwidget)
        self.player_score.setObjectName(u"player_score")
        self.player_score.setGeometry(QRect(90, 260, 91, 31))
        self.player_score.setFont(font1)
        self.player_score.setStyleSheet(u"color: rgb(255, 14, 58);")
        self.player_score.setAlignment(Qt.AlignCenter)
        self.restart = QPushButton(self.centralwidget)
        self.restart.setObjectName(u"restart")
        self.restart.setGeometry(QRect(10, 390, 235, 61))
        self.restart.setAutoFillBackground(False)
        self.restart.setStyleSheet(u"image: url(:/img/reset.jpg);\n"
"background:rgb(246,246,246);\n"
"")
        self.result = QLabel(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(0, 320, 251, 61))
        self.result.setFont(font)
        self.result.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.result.setAlignment(Qt.AlignCenter)
        self.cpu = QLabel(self.centralwidget)
        self.cpu.setObjectName(u"cpu")
        self.cpu.setGeometry(QRect(100, 70, 71, 71))
        self.cpu.setStyleSheet(u"border:2px dashed rgb(74,125,0);\n"
"")
        self.player = QLabel(self.centralwidget)
        self.player.setObjectName(u"player")
        self.player.setGeometry(QRect(100, 170, 71, 71))
        self.player.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.rock.raise_()
        self.paper.raise_()
        self.scissors.raise_()
        self.cpu_box.raise_()
        self.label.raise_()
        self.player_box.raise_()
        self.label_2.raise_()
        self.cpu_score.raise_()
        self.player_score.raise_()
        self.restart.raise_()
        self.cpu.raise_()
        self.player.raise_()
        self.result.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Rock Paper Scissors Game", None))
        self.rock.setText("")
        self.paper.setText("")
        self.scissors.setText("")
        self.cpu_box.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Computer", None))
        self.player_box.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Player", None))
        self.cpu_score.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.player_score.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.restart.setText("")
        self.result.setText("")
        self.cpu.setText("")
        self.player.setText("")
    # retranslateUi

