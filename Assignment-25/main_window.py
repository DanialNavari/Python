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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(606, 396)
        MainWindow.setMinimumSize(QSize(606, 396))
        MainWindow.setMaximumSize(QSize(606, 396))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 601, 391))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.btn_start_stopwatch = QPushButton(self.tab_3)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        self.btn_start_stopwatch.setGeometry(QRect(130, 210, 91, 41))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn_start_stopwatch.setFont(font)
        self.btn_stop_stopwatch = QPushButton(self.tab_3)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setGeometry(QRect(236, 210, 101, 41))
        self.btn_stop_stopwatch.setFont(font)
        self.btn_reset_stopwatch = QPushButton(self.tab_3)
        self.btn_reset_stopwatch.setObjectName(u"btn_reset_stopwatch")
        self.btn_reset_stopwatch.setGeometry(QRect(356, 210, 101, 41))
        self.btn_reset_stopwatch.setFont(font)
        self.lbl_stopwatch = QLabel(self.tab_3)
        self.lbl_stopwatch.setObjectName(u"lbl_stopwatch")
        self.lbl_stopwatch.setGeometry(QRect(230, 80, 121, 41))
        font1 = QFont()
        font1.setFamilies([u"Seven Segment"])
        font1.setPointSize(40)
        font1.setBold(True)
        self.lbl_stopwatch.setFont(font1)
        self.lbl_stopwatch.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.btn_reset_timer = QPushButton(self.tab_4)
        self.btn_reset_timer.setObjectName(u"btn_reset_timer")
        self.btn_reset_timer.setGeometry(QRect(370, 210, 101, 41))
        self.btn_reset_timer.setFont(font)
        self.btn_start_timer = QPushButton(self.tab_4)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setGeometry(QRect(144, 210, 91, 41))
        self.btn_start_timer.setFont(font)
        self.btn_stop_timer = QPushButton(self.tab_4)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        self.btn_stop_timer.setGeometry(QRect(250, 210, 101, 41))
        self.btn_stop_timer.setFont(font)
        self.tb_minute_timer = QLineEdit(self.tab_4)
        self.tb_minute_timer.setObjectName(u"tb_minute_timer")
        self.tb_minute_timer.setGeometry(QRect(260, 90, 81, 71))
        font2 = QFont()
        font2.setFamilies([u"Seven Segment"])
        font2.setPointSize(40)
        self.tb_minute_timer.setFont(font2)
        self.tb_minute_timer.setAlignment(Qt.AlignCenter)
        self.tb_second_timer = QLineEdit(self.tab_4)
        self.tb_second_timer.setObjectName(u"tb_second_timer")
        self.tb_second_timer.setGeometry(QRect(360, 90, 81, 71))
        self.tb_second_timer.setFont(font2)
        self.tb_second_timer.setAlignment(Qt.AlignCenter)
        self.tb_hour_timer = QLineEdit(self.tab_4)
        self.tb_hour_timer.setObjectName(u"tb_hour_timer")
        self.tb_hour_timer.setGeometry(QRect(160, 90, 81, 71))
        self.tb_hour_timer.setFont(font2)
        self.tb_hour_timer.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.lbl_stopwatch.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Stop Watch", None))
        self.btn_reset_timer.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tb_minute_timer.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.tb_second_timer.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.tb_hour_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

