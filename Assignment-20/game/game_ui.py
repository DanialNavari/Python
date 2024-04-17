# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(471, 426)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(-1, -1, 491, 431))
        self.groupBox.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(191, 80, 91, 80))
        self.cpu_1_select = QLabel(self.groupBox_2)
        self.cpu_1_select.setObjectName(u"cpu_1_select")
        self.cpu_1_select.setGeometry(QRect(8, 9, 71, 61))
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(33)
        self.cpu_1_select.setFont(font)
        self.cpu_1_select.setAlignment(Qt.AlignCenter)
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(190, 170, 91, 80))
        self.cpu_2_select = QLabel(self.groupBox_3)
        self.cpu_2_select.setObjectName(u"cpu_2_select")
        self.cpu_2_select.setGeometry(QRect(10, 10, 71, 61))
        self.cpu_2_select.setFont(font)
        self.cpu_2_select.setAlignment(Qt.AlignCenter)
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(190, 260, 91, 80))
        self.user_select = QLabel(self.groupBox_4)
        self.user_select.setObjectName(u"user_select")
        self.user_select.setGeometry(QRect(10, 10, 71, 61))
        self.user_select.setFont(font)
        self.user_select.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 10, 71, 31))
        font1 = QFont()
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(380, 190, 71, 31))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 390, 71, 31))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.cpu_2_point = QLabel(self.groupBox)
        self.cpu_2_point.setObjectName(u"cpu_2_point")
        self.cpu_2_point.setGeometry(QRect(380, 220, 71, 31))
        self.cpu_2_point.setFont(font1)
        self.cpu_2_point.setStyleSheet(u"color:rgb(255, 0, 0)")
        self.cpu_2_point.setAlignment(Qt.AlignCenter)
        self.cpu_1_point = QLabel(self.groupBox)
        self.cpu_1_point.setObjectName(u"cpu_1_point")
        self.cpu_1_point.setGeometry(QRect(200, 40, 71, 31))
        self.cpu_1_point.setFont(font1)
        self.cpu_1_point.setStyleSheet(u"color:rgb(255, 0, 0)")
        self.cpu_1_point.setAlignment(Qt.AlignCenter)
        self.user_point = QLabel(self.groupBox)
        self.user_point.setObjectName(u"user_point")
        self.user_point.setGeometry(QRect(200, 360, 71, 31))
        self.user_point.setFont(font1)
        self.user_point.setStyleSheet(u"color:rgb(255, 0, 0)")
        self.user_point.setAlignment(Qt.AlignCenter)
        self.inside = QPushButton(self.groupBox)
        self.inside.setObjectName(u"inside")
        self.inside.setGeometry(QRect(280, 350, 75, 71))
        font2 = QFont()
        font2.setPointSize(36)
        self.inside.setFont(font2)
        self.outside = QPushButton(self.groupBox)
        self.outside.setObjectName(u"outside")
        self.outside.setGeometry(QRect(120, 350, 75, 71))
        self.outside.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Palam Game", None))
        self.groupBox_2.setTitle("")
        self.cpu_1_select.setText("")
        self.groupBox_3.setTitle("")
        self.cpu_2_select.setText("")
        self.groupBox_4.setTitle("")
        self.user_select.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"CPU 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CPU 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"USER", None))
        self.cpu_2_point.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_1_point.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.user_point.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.inside.setText(QCoreApplication.translate("MainWindow", u" \u270b ", None))
        self.outside.setText(QCoreApplication.translate("MainWindow", u"\ud83e\udd1a", None))
    # retranslateUi

