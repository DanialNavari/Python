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
import bg_rc

class Ui_Winner(object):
    def setupUi(self, Winner):
        if not Winner.objectName():
            Winner.setObjectName(u"Winner")
        Winner.resize(451, 381)
        Winner.setMinimumSize(QSize(451, 381))
        Winner.setMaximumSize(QSize(451, 381))
        self.centralwidget = QWidget(Winner)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 451, 381))
        self.label.setMinimumSize(QSize(451, 381))
        self.label.setStyleSheet(u"image: url(:/bg/win.jpg);")
        self.label.setAlignment(Qt.AlignCenter)
        self.restart_btn = QPushButton(self.centralwidget)
        self.restart_btn.setObjectName(u"restart_btn")
        self.restart_btn.setGeometry(QRect(180, 310, 81, 41))
        font = QFont()
        font.setFamilies([u"B Nazanin"])
        font.setPointSize(12)
        font.setBold(True)
        self.restart_btn.setFont(font)
        Winner.setCentralWidget(self.centralwidget)

        self.retranslateUi(Winner)

        QMetaObject.connectSlotsByName(Winner)
    # setupUi

    def retranslateUi(self, Winner):
        Winner.setWindowTitle(QCoreApplication.translate("Winner", u"Winner!!!", None))
        self.label.setText("")
        self.restart_btn.setText(QCoreApplication.translate("Winner", u"\u0634\u0631\u0648\u0639 \u0645\u062c\u062f\u062f", None))
    # retranslateUi

