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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 556)
        self.menu_new = QAction(MainWindow)
        self.menu_new.setObjectName(u"menu_new")
        self.menu_open = QAction(MainWindow)
        self.menu_open.setObjectName(u"menu_open")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, -1, 761, 531))
        self.grid_layout = QGridLayout(self.gridLayoutWidget)
        self.grid_layout.setObjectName(u"grid_layout")
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 780, 22))
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName(u"menuGame")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuGame.menuAction())
        self.menuGame.addAction(self.menu_new)
        self.menuGame.addSeparator()
        self.menuGame.addAction(self.menu_open)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Suduku Game", None))
        self.menu_new.setText(QCoreApplication.translate("MainWindow", u"New...", None))
        self.menu_open.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
    # retranslateUi

