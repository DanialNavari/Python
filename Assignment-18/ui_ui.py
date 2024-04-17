# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QWidget)
import bg_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.ApplicationModal)
        Form.setEnabled(True)
        Form.resize(368, 431)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(368, 431))
        Form.setBaseSize(QSize(0, -1))
        Form.setCursor(QCursor(Qt.ArrowCursor))
        Form.setAcceptDrops(False)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color:#cacaca")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.xsign = QLabel(Form)
        self.xsign.setObjectName(u"xsign")
        self.xsign.setStyleSheet(u"image: url(X.png);")

        self.gridLayout.addWidget(self.xsign, 0, 0, 1, 1)

        self.Xscore = QLabel(Form)
        self.Xscore.setObjectName(u"Xscore")
        font = QFont()
        font.setFamilies([u"B Titr"])
        font.setPointSize(20)
        self.Xscore.setFont(font)
        self.Xscore.setLayoutDirection(Qt.RightToLeft)
        self.Xscore.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.Xscore.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Xscore, 0, 1, 1, 1)

        self.same = QLabel(Form)
        self.same.setObjectName(u"same")
        self.same.setFont(font)
        self.same.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.same.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.same, 0, 2, 1, 1)

        self.Oscore = QLabel(Form)
        self.Oscore.setObjectName(u"Oscore")
        self.Oscore.setFont(font)
        self.Oscore.setStyleSheet(u"color:red;")
        self.Oscore.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Oscore, 0, 3, 1, 1)

        self.osign = QLabel(Form)
        self.osign.setObjectName(u"osign")
        self.osign.setStyleSheet(u"image: url(o1.png);")

        self.gridLayout.addWidget(self.osign, 0, 4, 1, 1)

        self.btn_1 = QPushButton(Form)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.btn_1.setFont(font1)

        self.gridLayout.addWidget(self.btn_1, 1, 0, 1, 1)

        self.btn_2 = QPushButton(Form)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy1.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy1)
        self.btn_2.setFont(font1)
        self.btn_2.setStyleSheet(u"color: rgb(35, 31, 32);")

        self.gridLayout.addWidget(self.btn_2, 1, 1, 1, 3)

        self.btn_3 = QPushButton(Form)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy1.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy1)
        self.btn_3.setFont(font1)
        self.btn_3.setStyleSheet(u"color: rgb(35, 31, 32);")

        self.gridLayout.addWidget(self.btn_3, 1, 4, 1, 1)

        self.btn_4 = QPushButton(Form)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy1.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy1)
        self.btn_4.setFont(font1)
        self.btn_4.setStyleSheet(u"color: rgb(35, 31, 32);")

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_5 = QPushButton(Form)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy1.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy1)
        self.btn_5.setFont(font1)
        self.btn_5.setStyleSheet(u"color: rgb(35, 31, 32);")

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 3)

        self.btn_6 = QPushButton(Form)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy1.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy1)
        self.btn_6.setFont(font1)
        self.btn_6.setStyleSheet(u"color: rgb(35, 31, 32);")

        self.gridLayout.addWidget(self.btn_6, 2, 4, 1, 1)

        self.btn_7 = QPushButton(Form)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy1.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy1)
        self.btn_7.setFont(font1)
        self.btn_7.setStyleSheet(u"color: rgb(35, 31, 32);")

        self.gridLayout.addWidget(self.btn_7, 3, 0, 1, 1)

        self.btn_8 = QPushButton(Form)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy1.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy1)
        self.btn_8.setFont(font1)
        self.btn_8.setStyleSheet(u"color: rgb(35, 31, 32);")

        self.gridLayout.addWidget(self.btn_8, 3, 1, 1, 3)

        self.btn_9 = QPushButton(Form)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy1.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy1)
        self.btn_9.setFont(font1)
        self.btn_9.setStyleSheet(u"color: rgb(35, 31, 32);")

        self.gridLayout.addWidget(self.btn_9, 3, 4, 1, 1)

        self.vsplayer = QRadioButton(Form)
        self.vsplayer.setObjectName(u"vsplayer")
        font2 = QFont()
        font2.setFamilies([u"Yekan Bakh FaNum Black"])
        font2.setPointSize(11)
        self.vsplayer.setFont(font2)
        self.vsplayer.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.vsplayer, 4, 0, 1, 1)

        self.mov = QLabel(Form)
        self.mov.setObjectName(u"mov")

        self.gridLayout.addWidget(self.mov, 4, 1, 1, 1)

        self.vscomputer = QRadioButton(Form)
        self.vscomputer.setObjectName(u"vscomputer")
        self.vscomputer.setFont(font2)
        self.vscomputer.setLayoutDirection(Qt.RightToLeft)
        self.vscomputer.setChecked(False)

        self.gridLayout.addWidget(self.vscomputer, 4, 4, 1, 1)

        self.restart = QPushButton(Form)
        self.restart.setObjectName(u"restart")
        sizePolicy1.setHeightForWidth(self.restart.sizePolicy().hasHeightForWidth())
        self.restart.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Yekan Bakh FaNum Black"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.restart.setFont(font3)
        self.restart.setStyleSheet(u"color:red")

        self.gridLayout.addWidget(self.restart, 5, 0, 1, 1)

        self.vs = QLabel(Form)
        self.vs.setObjectName(u"vs")

        self.gridLayout.addWidget(self.vs, 5, 1, 1, 1)

        self.about = QPushButton(Form)
        self.about.setObjectName(u"about")
        sizePolicy1.setHeightForWidth(self.about.sizePolicy().hasHeightForWidth())
        self.about.setSizePolicy(sizePolicy1)
        self.about.setFont(font3)
        self.about.setStyleSheet(u"color:darkgreen")

        self.gridLayout.addWidget(self.about, 5, 4, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Tick Toc Toe", None))
        self.xsign.setText("")
        self.Xscore.setText(QCoreApplication.translate("Form", u"0", None))
        self.same.setText(QCoreApplication.translate("Form", u"0", None))
        self.Oscore.setText(QCoreApplication.translate("Form", u"0", None))
        self.osign.setText("")
        self.btn_1.setText("")
        self.btn_2.setText("")
        self.btn_3.setText("")
        self.btn_4.setText("")
        self.btn_5.setText("")
        self.btn_6.setText("")
        self.btn_7.setText("")
        self.btn_8.setText("")
        self.btn_9.setText("")
        self.vsplayer.setText(QCoreApplication.translate("Form", u"\u0628\u0627\u0632\u06cc \u062f\u0648 \u0646\u0641\u0631\u0647", None))
        self.mov.setText("")
        self.vscomputer.setText(QCoreApplication.translate("Form", u"\u0628\u0627\u0632\u06cc \u0628\u0627 \u06a9\u0627\u0645\u067e\u06cc\u0648\u062a\u0631", None))
        self.restart.setText(QCoreApplication.translate("Form", u"\u0634\u0631\u0648\u0639 \u0645\u062c\u062f\u062f \u0628\u0627\u0632\u06cc", None))
        self.vs.setText("")
        self.about.setText(QCoreApplication.translate("Form", u"\u062f\u0631\u0628\u0627\u0631\u0647 \u0628\u0627\u0632\u06cc", None))
    # retranslateUi

