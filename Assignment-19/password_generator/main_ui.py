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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(298, 196)
        MainWindow.setMinimumSize(QSize(298, 196))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Yekan Bakh FaNum"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.radio_super = QRadioButton(self.centralwidget)
        self.radio_super.setObjectName(u"radio_super")
        font1 = QFont()
        font1.setFamilies([u"Yekan Bakh FaNum"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.radio_super.setFont(font1)
        self.radio_super.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.radio_super, 1, 0, 1, 1)

        self.radio_strong = QRadioButton(self.centralwidget)
        self.radio_strong.setObjectName(u"radio_strong")
        self.radio_strong.setFont(font1)
        self.radio_strong.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.radio_strong, 1, 1, 1, 1)

        self.radio_standard = QRadioButton(self.centralwidget)
        self.radio_standard.setObjectName(u"radio_standard")
        self.radio_standard.setFont(font1)
        self.radio_standard.setLayoutDirection(Qt.RightToLeft)
        self.radio_standard.setChecked(True)

        self.gridLayout.addWidget(self.radio_standard, 1, 2, 1, 1)

        self.password = QTextEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setEnabled(True)
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.password.setFont(font2)
        self.password.setReadOnly(True)

        self.gridLayout.addWidget(self.password, 2, 0, 1, 3)

        self.btn_generate = QPushButton(self.centralwidget)
        self.btn_generate.setObjectName(u"btn_generate")
        font3 = QFont()
        font3.setFamilies([u"Yekan Bakh FaNum"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.btn_generate.setFont(font3)

        self.gridLayout.addWidget(self.btn_generate, 3, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0645\u06cc\u0632\u0627\u0646 \u0633\u062e\u062a\u06cc \u0631\u0645\u0632 \u0639\u0628\u0648\u0631 \u0631\u0627 \u0627\u0646\u062a\u062e\u0627\u0628 \u06a9\u0646\u06cc\u062f:", None))
        self.radio_super.setText(QCoreApplication.translate("MainWindow", u"\u062e\u06cc\u0644\u06cc \u067e\u06cc\u0686\u06cc\u062f\u0647", None))
        self.radio_strong.setText(QCoreApplication.translate("MainWindow", u"\u067e\u06cc\u0686\u06cc\u062f\u0647", None))
        self.radio_standard.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u062a\u0627\u0646\u062f\u0627\u0631\u062f", None))
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u"\u0627\u06cc\u062c\u0627\u062f \u0631\u0645\u0632 \u0639\u0628\u0648\u0631", None))
    # retranslateUi

