# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_new_task.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
import bg_rc

class Ui_MainWindow_task(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(277, 462)
        MainWindow.setMinimumSize(QSize(277, 462))
        MainWindow.setMaximumSize(QSize(277, 462))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 20, 261, 351))
        font = QFont()
        font.setFamilies([u"Yekan Bakh FaNum Black"])
        font.setPointSize(11)
        font.setBold(True)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.tb_new_task = QLineEdit(self.verticalLayoutWidget)
        self.tb_new_task.setObjectName(u"tb_new_task")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_new_task.sizePolicy().hasHeightForWidth())
        self.tb_new_task.setSizePolicy(sizePolicy)
        self.tb_new_task.setMinimumSize(QSize(0, 30))
        self.tb_new_task.setFont(font)

        self.verticalLayout_2.addWidget(self.tb_new_task)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.tb_new_desc = QTextEdit(self.verticalLayoutWidget)
        self.tb_new_desc.setObjectName(u"tb_new_desc")
        self.tb_new_desc.setFont(font)

        self.verticalLayout_2.addWidget(self.tb_new_desc)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setLineWidth(0)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rb_normal = QRadioButton(self.verticalLayoutWidget)
        self.rb_normal.setObjectName(u"rb_normal")
        self.rb_normal.setFont(font)
        self.rb_normal.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout.addWidget(self.rb_normal)

        self.rb_important = QRadioButton(self.verticalLayoutWidget)
        self.rb_important.setObjectName(u"rb_important")
        self.rb_important.setFont(font)
        self.rb_important.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout.addWidget(self.rb_important)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tb_hafte = QLineEdit(self.verticalLayoutWidget)
        self.tb_hafte.setObjectName(u"tb_hafte")
        sizePolicy.setHeightForWidth(self.tb_hafte.sizePolicy().hasHeightForWidth())
        self.tb_hafte.setSizePolicy(sizePolicy)
        self.tb_hafte.setMinimumSize(QSize(0, 30))
        self.tb_hafte.setFont(font)

        self.horizontalLayout_2.addWidget(self.tb_hafte)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tarikh = QLineEdit(self.verticalLayoutWidget)
        self.tarikh.setObjectName(u"tarikh")
        sizePolicy.setHeightForWidth(self.tarikh.sizePolicy().hasHeightForWidth())
        self.tarikh.setSizePolicy(sizePolicy)
        self.tarikh.setMinimumSize(QSize(0, 30))
        self.tarikh.setFont(font)

        self.horizontalLayout_3.addWidget(self.tarikh)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.saat = QLineEdit(self.verticalLayoutWidget)
        self.saat.setObjectName(u"saat")
        sizePolicy.setHeightForWidth(self.saat.sizePolicy().hasHeightForWidth())
        self.saat.setSizePolicy(sizePolicy)
        self.saat.setMinimumSize(QSize(0, 30))
        self.saat.setFont(font)

        self.horizontalLayout_4.addWidget(self.saat)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setGeometry(QRect(180, 380, 71, 71))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy1)
        self.save_btn.setMinimumSize(QSize(0, 30))
        self.save_btn.setMaximumSize(QSize(16777215, 16777215))
        self.save_btn.setFont(font)
        self.save_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_btn.setStyleSheet(u"image: url(:/btn/check.png);  \n"
"border:none;\n"
"")
        self.back_btn = QPushButton(self.centralwidget)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(20, 380, 71, 71))
        self.back_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_btn.setStyleSheet(u"border:none;\n"
"image: url(:/btn/back.png);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"To Do List", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0646\u0648\u0627\u0646 \u0641\u0639\u0627\u0644\u06cc\u062a:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u062d \u0641\u0639\u0627\u0644\u06cc\u062a:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0648\u0639 \u0641\u0639\u0627\u0644\u06cc\u062a:", None))
        self.rb_normal.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0627\u062f\u06cc", None))
        self.rb_important.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0647\u0645", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0648\u0632 \u0647\u0641\u062a\u0647:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u0639\u062a:", None))
        self.save_btn.setText("")
        self.back_btn.setText("")
    # retranslateUi

