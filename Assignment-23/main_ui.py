# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QMainWindow,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 555)
        MainWindow.setMinimumSize(QSize(780, 555))
        MainWindow.setMaximumSize(QSize(780, 555))
        self.menu_new = QAction(MainWindow)
        self.menu_new.setObjectName("menu_new")
        self.menu_open = QAction(MainWindow)
        self.menu_open.setObjectName("menu_open")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName("line_3")
        self.line_3.setGeometry(QRect(0, 177, 781, 10))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName("line_4")
        self.line_4.setGeometry(QRect(0, 352, 781, 10))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(260, 0, 16, 541))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName("line_2")
        self.line_2.setGeometry(QRect(505, 0, 16, 541))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 761, 521))
        self.grid_layout = QGridLayout(self.gridLayoutWidget)
        self.grid_layout.setObjectName("grid_layout")
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 780, 22))
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName("menuGame")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuGame.menuAction())
        self.menuGame.addAction(self.menu_new)
        self.menuGame.addSeparator()
        self.menuGame.addAction(self.menu_open)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Sudoku Game", None)
        )
        self.menu_new.setText(QCoreApplication.translate("MainWindow", "New...", None))
        self.menu_open.setText(
            QCoreApplication.translate("MainWindow", "Open File", None)
        )
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", "Game", None))

    # retranslateUi
