# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
    QSizePolicy, QSpinBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(308, 133)
        MainWindow.setMaximumSize(QSize(308, 133))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 291, 29))
        font = QFont()
        font.setFamilies([u"Yekan Bakh FaNum"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.btn_check = QPushButton(self.centralwidget)
        self.btn_check.setObjectName(u"btn_check")
        self.btn_check.setGeometry(QRect(10, 90, 291, 33))
        font1 = QFont()
        font1.setFamilies([u"Yekan Bakh FaNum"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.btn_check.setFont(font1)
        self.word = QSpinBox(self.centralwidget)
        self.word.setObjectName(u"word")
        self.word.setGeometry(QRect(10, 40, 291, 41))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.word.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u062f \u0645\u0648\u0631\u062f \u0646\u0638\u0631 \u0631\u0627 \u062d\u062f\u0633 \u0628\u0632\u0646\u06cc\u062f!!", None))
        self.btn_check.setText(QCoreApplication.translate("MainWindow", u"\u0686\u06a9 \u06a9\u0646", None))
    # retranslateUi

