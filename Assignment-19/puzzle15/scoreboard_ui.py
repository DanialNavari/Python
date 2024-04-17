# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scoreboard.ui'
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
import bg_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(501, 427)
        MainWindow.setMinimumSize(QSize(501, 427))
        MainWindow.setMaximumSize(QSize(501, 427))
        MainWindow.setStyleSheet(u"background-color: rgb(51, 50, 51);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 483, 381))
        self.label.setStyleSheet(u"image: url(:/bg/bgg.png);")
        self.s4 = QLabel(self.centralwidget)
        self.s4.setObjectName(u"s4")
        self.s4.setGeometry(QRect(190, 200, 21, 51))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.s4.setFont(font)
        self.s4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.s4.setAlignment(Qt.AlignCenter)
        self.s3 = QLabel(self.centralwidget)
        self.s3.setObjectName(u"s3")
        self.s3.setGeometry(QRect(225, 200, 21, 51))
        self.s3.setFont(font)
        self.s3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.s3.setAlignment(Qt.AlignCenter)
        self.s2 = QLabel(self.centralwidget)
        self.s2.setObjectName(u"s2")
        self.s2.setGeometry(QRect(258, 200, 21, 51))
        self.s2.setFont(font)
        self.s2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.s2.setAlignment(Qt.AlignCenter)
        self.s1 = QLabel(self.centralwidget)
        self.s1.setObjectName(u"s1")
        self.s1.setGeometry(QRect(290, 200, 21, 51))
        self.s1.setFont(font)
        self.s1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.s1.setAlignment(Qt.AlignCenter)
        self.hh = QLabel(self.centralwidget)
        self.hh.setObjectName(u"hh")
        self.hh.setGeometry(QRect(180, 85, 21, 51))
        self.hh.setFont(font)
        self.hh.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.hh.setAlignment(Qt.AlignCenter)
        self.h = QLabel(self.centralwidget)
        self.h.setObjectName(u"h")
        self.h.setGeometry(QRect(216, 85, 21, 51))
        self.h.setFont(font)
        self.h.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.h.setAlignment(Qt.AlignCenter)
        self.mm = QLabel(self.centralwidget)
        self.mm.setObjectName(u"mm")
        self.mm.setGeometry(QRect(265, 85, 21, 51))
        self.mm.setFont(font)
        self.mm.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.mm.setAlignment(Qt.AlignCenter)
        self.m = QLabel(self.centralwidget)
        self.m.setObjectName(u"m")
        self.m.setGeometry(QRect(303, 85, 21, 51))
        self.m.setFont(font)
        self.m.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.m.setAlignment(Qt.AlignCenter)
        self.btn_retrn = QPushButton(self.centralwidget)
        self.btn_retrn.setObjectName(u"btn_retrn")
        self.btn_retrn.setGeometry(QRect(180, 370, 121, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_retrn.sizePolicy().hasHeightForWidth())
        self.btn_retrn.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"B Yekan"])
        font1.setPointSize(16)
        self.btn_retrn.setFont(font1)
        self.btn_retrn.setStyleSheet(u"background-color: rgb(78, 76, 78);\n"
"color: rgb(255, 255, 255);")
        self.m1 = QLabel(self.centralwidget)
        self.m1.setObjectName(u"m1")
        self.m1.setGeometry(QRect(285, 295, 21, 51))
        self.m1.setFont(font)
        self.m1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.m1.setAlignment(Qt.AlignCenter)
        self.m2 = QLabel(self.centralwidget)
        self.m2.setObjectName(u"m2")
        self.m2.setGeometry(QRect(257, 295, 21, 51))
        self.m2.setFont(font)
        self.m2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.m2.setAlignment(Qt.AlignCenter)
        self.m4 = QLabel(self.centralwidget)
        self.m4.setObjectName(u"m4")
        self.m4.setGeometry(QRect(203, 295, 21, 51))
        self.m4.setFont(font)
        self.m4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.m4.setAlignment(Qt.AlignCenter)
        self.m3 = QLabel(self.centralwidget)
        self.m3.setObjectName(u"m3")
        self.m3.setGeometry(QRect(230, 295, 21, 51))
        self.m3.setFont(font)
        self.m3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.m3.setAlignment(Qt.AlignCenter)
        self.elaps_time = QLabel(self.centralwidget)
        self.elaps_time.setObjectName(u"elaps_time")
        self.elaps_time.setGeometry(QRect(360, 70, 49, 16))
        self.elaps_time.setStyleSheet(u"opacity:1;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.s4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.s3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.s2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.s1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.hh.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.h.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.mm.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.m.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_retrn.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632\u06af\u0634\u062a", None))
        self.m1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.m2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.m4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.m3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.elaps_time.setText("")
    # retranslateUi

