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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(332, 225)
        mainWindow.setMinimumSize(QSize(332, 225))
        mainWindow.setMaximumSize(QSize(332, 225))
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 311, 51))
        self.combo_units = QComboBox(self.groupBox)
        self.combo_units.addItem("")
        self.combo_units.addItem("")
        self.combo_units.addItem("")
        self.combo_units.addItem("")
        self.combo_units.setObjectName(u"combo_units")
        self.combo_units.setGeometry(QRect(30, 10, 191, 31))
        font = QFont()
        font.setFamilies([u"Yekan Bakh FaNum"])
        font.setPointSize(12)
        font.setBold(True)
        self.combo_units.setFont(font)
        self.combo_units.setLayoutDirection(Qt.RightToLeft)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 15, 71, 21))
        font1 = QFont()
        font1.setFamilies([u"Yekan Bakh FaNum"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label.setFont(font1)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 70, 311, 151))
        self.combo_from = QComboBox(self.groupBox_2)
        self.combo_from.setObjectName(u"combo_from")
        self.combo_from.setGeometry(QRect(140, 10, 131, 31))
        self.combo_from.setFont(font)
        self.combo_from.setLayoutDirection(Qt.RightToLeft)
        self.combo_to = QComboBox(self.groupBox_2)
        self.combo_to.setObjectName(u"combo_to")
        self.combo_to.setGeometry(QRect(140, 70, 131, 31))
        self.combo_to.setFont(font)
        self.combo_to.setLayoutDirection(Qt.RightToLeft)
        self.cal = QPushButton(self.groupBox_2)
        self.cal.setObjectName(u"cal")
        self.cal.setGeometry(QRect(14, 110, 261, 41))
        self.cal.setFont(font)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 50, 21, 21))
        self.label_2.setFont(font1)
        self.text_from = QLineEdit(self.groupBox_2)
        self.text_from.setObjectName(u"text_from")
        self.text_from.setGeometry(QRect(20, 10, 113, 31))
        self.text_from.setFont(font1)
        self.text_to = QLineEdit(self.groupBox_2)
        self.text_to.setObjectName(u"text_to")
        self.text_to.setEnabled(False)
        self.text_to.setGeometry(QRect(20, 70, 113, 31))
        self.text_to.setFont(font1)
        self.text_to.setReadOnly(True)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Unit Converter", None))
        self.groupBox.setTitle("")
        self.combo_units.setItemText(0, QCoreApplication.translate("mainWindow", u"\u0648\u0632\u0646", None))
        self.combo_units.setItemText(1, QCoreApplication.translate("mainWindow", u"\u0637\u0648\u0644", None))
        self.combo_units.setItemText(2, QCoreApplication.translate("mainWindow", u"\u062f\u0645\u0627", None))
        self.combo_units.setItemText(3, QCoreApplication.translate("mainWindow", u"\u062d\u062c\u0645 \u062f\u06cc\u062c\u06cc\u062a\u0627\u0644\u06cc", None))

        self.label.setText(QCoreApplication.translate("mainWindow", u"\u062a\u0628\u062f\u06cc\u0644 :", None))
        self.groupBox_2.setTitle("")
        self.cal.setText(QCoreApplication.translate("mainWindow", u"\u0645\u062d\u0627\u0633\u0628\u0647", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"=", None))
    # retranslateUi

