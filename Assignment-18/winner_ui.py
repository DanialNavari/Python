# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'winner.ui'
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
import winner_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(501, 500)
        MainWindow.setMinimumSize(QSize(501, 500))
        MainWindow.setMaximumSize(QSize(501, 500))
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"background-color:#fff;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.result = QLabel(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(140, 200, 211, 42))
        font = QFont()
        font.setFamilies([u"Yekan Bakh FaNum Black"])
        font.setPointSize(20)
        self.result.setFont(font)
        self.result.setStyleSheet(u"color:red;")
        self.result.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(11, 9, 481, 188))
        self.label_2.setStyleSheet(u"image: url(winner.jpg) 100% 100%;")
        self.new_game = QPushButton(self.centralwidget)
        self.new_game.setObjectName(u"new_game")
        self.new_game.setGeometry(QRect(144, 250, 201, 41))
        font1 = QFont()
        font1.setFamilies([u"Yekan Bakh FaNum Black"])
        font1.setPointSize(13)
        self.new_game.setFont(font1)
        self.new_game.setStyleSheet(u"background-color:pink;\n"
"color: rgb(85, 0, 127);")
        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setEnabled(True)
        self.btn_7.setGeometry(QRect(60, 420, 113, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(True)
        self.btn_7.setFont(font2)
        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setEnabled(True)
        self.btn_8.setGeometry(QRect(180, 420, 112, 61))
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setFont(font2)
        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setEnabled(True)
        self.btn_5.setGeometry(QRect(180, 360, 112, 60))
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setFont(font2)
        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setEnabled(True)
        self.btn_6.setGeometry(QRect(300, 360, 113, 60))
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setFont(font2)
        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setEnabled(True)
        self.btn_9.setGeometry(QRect(300, 420, 113, 61))
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setFont(font2)
        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setEnabled(True)
        self.btn_2.setGeometry(QRect(180, 300, 112, 61))
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setFont(font2)
        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setEnabled(True)
        self.btn_4.setGeometry(QRect(60, 360, 113, 60))
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setFont(font2)
        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setEnabled(True)
        self.btn_3.setGeometry(QRect(300, 300, 113, 61))
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setFont(font2)
        self.btn_3.setStyleSheet(u"background-color:transparent;\n"
"border:none")
        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setEnabled(True)
        self.btn_1.setGeometry(QRect(60, 300, 113, 61))
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(30)
        font3.setBold(True)
        font3.setStrikeOut(False)
        self.btn_1.setFont(font3)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 300, 411, 191))
        self.label.setStyleSheet(u"background-color:transparent;\n"
"border:none")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.result.raise_()
        self.new_game.raise_()
        self.btn_7.raise_()
        self.btn_8.raise_()
        self.btn_5.raise_()
        self.btn_6.raise_()
        self.btn_9.raise_()
        self.btn_2.raise_()
        self.btn_4.raise_()
        self.btn_3.raise_()
        self.btn_1.raise_()
        self.label.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.result.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632\u06cc\u06a9\u0646 2 \u0628\u0631\u0646\u062f\u0647 \u0627\u0633\u062a", None))
        self.label_2.setText("")
        self.new_game.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632\u06cc \u062c\u062f\u06cc\u062f", None))
        self.btn_7.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color:transparent;\n"
"border:none", None))
        self.btn_7.setText("")
        self.btn_8.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color:transparent;\n"
"border:none", None))
        self.btn_8.setText("")
        self.btn_5.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color:transparent;\n"
"border:none", None))
        self.btn_5.setText("")
        self.btn_6.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color:transparent;\n"
"border:none", None))
        self.btn_6.setText("")
        self.btn_9.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color:transparent;\n"
"border:none", None))
        self.btn_9.setText("")
        self.btn_2.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color:transparent;\n"
"border:none", None))
        self.btn_2.setText("")
        self.btn_4.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color:transparent;\n"
"border:none", None))
        self.btn_4.setText("")
        self.btn_3.setText("")
        self.btn_1.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color:transparent;\n"
"border:none", None))
        self.btn_1.setText("")
        self.label.setText("")
    # retranslateUi

