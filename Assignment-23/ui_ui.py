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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 555)
        MainWindow.setMinimumSize(QSize(780, 555))
        MainWindow.setMaximumSize(QSize(780, 555))
        self.menu_new = QAction(MainWindow)
        self.menu_new.setObjectName(u"menu_new")
        self.menu_open = QAction(MainWindow)
        self.menu_open.setObjectName(u"menu_open")
        self.actionVery_Easy = QAction(MainWindow)
        self.actionVery_Easy.setObjectName(u"actionVery_Easy")
        self.actionEasy = QAction(MainWindow)
        self.actionEasy.setObjectName(u"actionEasy")
        self.actionNormal = QAction(MainWindow)
        self.actionNormal.setObjectName(u"actionNormal")
        self.actionHard = QAction(MainWindow)
        self.actionHard.setObjectName(u"actionHard")
        self.actionVery_Hard = QAction(MainWindow)
        self.actionVery_Hard.setObjectName(u"actionVery_Hard")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 180, 761, 10))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 350, 771, 10))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(260, 0, 16, 541))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(500, 0, 16, 541))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 761, 521))
        self.grid_layout = QGridLayout(self.gridLayoutWidget)
        self.grid_layout.setObjectName(u"grid_layout")
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 780, 22))
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName(u"menuGame")
        self.menuDifficulty = QMenu(self.menuGame)
        self.menuDifficulty.setObjectName(u"menuDifficulty")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuGame.menuAction())
        self.menuGame.addAction(self.menu_new)
        self.menuGame.addSeparator()
        self.menuGame.addAction(self.menu_open)
        self.menuGame.addAction(self.menuDifficulty.menuAction())
        self.menuDifficulty.addAction(self.actionVery_Easy)
        self.menuDifficulty.addAction(self.actionEasy)
        self.menuDifficulty.addAction(self.actionNormal)
        self.menuDifficulty.addAction(self.actionHard)
        self.menuDifficulty.addAction(self.actionVery_Hard)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sudoku Game", None))
        self.menu_new.setText(QCoreApplication.translate("MainWindow", u"New...", None))
        self.menu_open.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionVery_Easy.setText(QCoreApplication.translate("MainWindow", u"Very Easy", None))
        self.actionEasy.setText(QCoreApplication.translate("MainWindow", u"Easy", None))
        self.actionNormal.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.actionHard.setText(QCoreApplication.translate("MainWindow", u"Hard", None))
        self.actionVery_Hard.setText(QCoreApplication.translate("MainWindow", u"Very Hard", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.menuDifficulty.setTitle(QCoreApplication.translate("MainWindow", u"Difficulty", None))
    # retranslateUi

