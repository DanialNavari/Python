# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alarm.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(623, 402)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 591, 381))
        font = QFont()
        font.setFamilies([u"IRANYekanX"])
        font.setPointSize(12)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.edit_widget = QTabWidget(self.tab_2)
        self.edit_widget.setObjectName(u"edit_widget")
        self.edit_widget.setGeometry(QRect(340, 10, 231, 151))
        font1 = QFont()
        font1.setFamilies([u"IRANYekanX"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.edit_widget.setFont(font1)
        self.edit_widget.setElideMode(Qt.ElideNone)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 20, 81, 16))
        self.label.setFont(font)
        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 50, 81, 16))
        self.label_2.setFont(font)
        self.alarm_name = QLineEdit(self.tab_3)
        self.alarm_name.setObjectName(u"alarm_name")
        self.alarm_name.setEnabled(False)
        self.alarm_name.setGeometry(QRect(92, 20, 131, 20))
        self.alarm_name.setFont(font)
        self.btn_edit_alarm = QPushButton(self.tab_3)
        self.btn_edit_alarm.setObjectName(u"btn_edit_alarm")
        self.btn_edit_alarm.setEnabled(False)
        self.btn_edit_alarm.setGeometry(QRect(4, 80, 221, 31))
        self.btn_edit_alarm.setFont(font1)
        self.alarm_hour_set = QSpinBox(self.tab_3)
        self.alarm_hour_set.setObjectName(u"alarm_hour_set")
        self.alarm_hour_set.setEnabled(False)
        self.alarm_hour_set.setGeometry(QRect(90, 50, 51, 22))
        self.alarm_minute_set = QSpinBox(self.tab_3)
        self.alarm_minute_set.setObjectName(u"alarm_minute_set")
        self.alarm_minute_set.setEnabled(False)
        self.alarm_minute_set.setGeometry(QRect(160, 50, 51, 22))
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 55, 31, 16))
        self.label_3.setFont(font)
        self.edit_widget.addTab(self.tab_3, "")
        self.gridLayoutWidget = QWidget(self.tab_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 286, 347))
        self.gridLayoutWidget.setFont(font)
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_4 = QFrame(self.gridLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.alarm_time_1 = QLabel(self.gridLayoutWidget)
        self.alarm_time_1.setObjectName(u"alarm_time_1")
        font2 = QFont()
        font2.setFamilies([u"IRANYekanX"])
        font2.setPointSize(22)
        font2.setBold(True)
        self.alarm_time_1.setFont(font2)

        self.verticalLayout.addWidget(self.alarm_time_1)

        self.alarm_text_1 = QLabel(self.gridLayoutWidget)
        self.alarm_text_1.setObjectName(u"alarm_text_1")
        self.alarm_text_1.setFont(font)
        self.alarm_text_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.alarm_text_1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.chk_active_1 = QCheckBox(self.gridLayoutWidget)
        self.chk_active_1.setObjectName(u"chk_active_1")
        self.chk_active_1.setFont(font1)

        self.horizontalLayout.addWidget(self.chk_active_1)

        self.btn_edit_1 = QPushButton(self.gridLayoutWidget)
        self.btn_edit_1.setObjectName(u"btn_edit_1")
        self.btn_edit_1.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_edit_1)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.alarm_time_2 = QLabel(self.gridLayoutWidget)
        self.alarm_time_2.setObjectName(u"alarm_time_2")
        self.alarm_time_2.setFont(font2)

        self.verticalLayout_2.addWidget(self.alarm_time_2)

        self.alarm_text_2 = QLabel(self.gridLayoutWidget)
        self.alarm_text_2.setObjectName(u"alarm_text_2")
        self.alarm_text_2.setFont(font)
        self.alarm_text_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.alarm_text_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.chk_active_2 = QCheckBox(self.gridLayoutWidget)
        self.chk_active_2.setObjectName(u"chk_active_2")
        self.chk_active_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.chk_active_2)

        self.btn_edit_2 = QPushButton(self.gridLayoutWidget)
        self.btn_edit_2.setObjectName(u"btn_edit_2")
        self.btn_edit_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.btn_edit_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.alarm_time_3 = QLabel(self.gridLayoutWidget)
        self.alarm_time_3.setObjectName(u"alarm_time_3")
        self.alarm_time_3.setFont(font2)

        self.verticalLayout_3.addWidget(self.alarm_time_3)

        self.alarm_text_3 = QLabel(self.gridLayoutWidget)
        self.alarm_text_3.setObjectName(u"alarm_text_3")
        self.alarm_text_3.setFont(font)
        self.alarm_text_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.alarm_text_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.chk_active_3 = QCheckBox(self.gridLayoutWidget)
        self.chk_active_3.setObjectName(u"chk_active_3")
        self.chk_active_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.chk_active_3)

        self.btn_edit_3 = QPushButton(self.gridLayoutWidget)
        self.btn_edit_3.setObjectName(u"btn_edit_3")
        self.btn_edit_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.btn_edit_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_3, 4, 0, 1, 1)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 1)

        self.line_3 = QFrame(self.gridLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 5, 0, 1, 1)

        self.line_5 = QFrame(self.tab_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(310, 10, 20, 341))
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0647\u0634\u062f\u0627\u0631", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0632\u0645\u0627\u0646 \u0647\u0634\u062f\u0627\u0631", None))
        self.btn_edit_alarm.setText(QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634 \u0647\u0634\u062f\u0627\u0631", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.edit_widget.setTabText(self.edit_widget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"                               \u0648\u06cc\u0631\u0627\u06cc\u0634 \u0647\u0634\u062f\u0627\u0631                                ", None))
        self.alarm_time_1.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.alarm_text_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chk_active_1.setText(QCoreApplication.translate("MainWindow", u"Active / Deactive", None))
        self.btn_edit_1.setText(QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634", None))
        self.alarm_time_2.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.alarm_text_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chk_active_2.setText(QCoreApplication.translate("MainWindow", u"Active / Deactive", None))
        self.btn_edit_2.setText(QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634", None))
        self.alarm_time_3.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.alarm_text_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chk_active_3.setText(QCoreApplication.translate("MainWindow", u"Active / Deactive", None))
        self.btn_edit_3.setText(QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"                                                                                             \u0622\u0644\u0627\u0631\u0645                                                                                      ", None))
    # retranslateUi

