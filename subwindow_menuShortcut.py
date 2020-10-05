import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class SubWindow_MenuShortcut(QDialog):  # QDialog
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.setWindowTitle('MENU')
        #self.resize(340, 280)
        self.resize(670, 645)
        self.setStyleSheet('background-color:white;')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        ## 상단 타이틀 바
        self.label_titlebar = QtWidgets.QLabel(self)
        self.label_titlebar.setObjectName("label_titlebar")
        self.label_titlebar.setMaximumHeight(90)
        self.label_titlebar.setStyleSheet('background-color:#B5A4E7')

        self.pushButton_Close = QtWidgets.QPushButton(self)
        self.pushButton_Close.setGeometry(QtCore.QRect(570, 0, 100, 90))
        self.pushButton_Close.setObjectName("pushButton_Close")
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        self.pushButton_Close.setFont(font)
        self.pushButton_Close.setText("×")
        self.pushButton_Close.setStyleSheet("background-color:#B5A4E7;"
                                            "color:white;"
                                            "border-width: 10px;"
                                            "border-color: #white;"
                                            )
        self.pushButton_Close.clicked.connect(self.CloseClieked)

        ## 메뉴모음
        self.pushButton_GoHome = QtWidgets.QPushButton(self)
        self.pushButton_GoHome.setObjectName("pushButton_GoHome")
        self.pushButton_GoHome.setMinimumHeight(220)
        self.pushButton_GoHome.setStyleSheet("border-image: url(image/menu_btn_home.png);")
        self.pushButton_GoHome.clicked.connect(self.HomeClieked)

        self.pushButton_GoMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMenu.setObjectName("pushButton_GoMenu")
        self.pushButton_GoMenu.setMinimumHeight(220)
        self.pushButton_GoMenu.setStyleSheet("border-image: url(image/menu_btn_menu.png);")
        self.pushButton_GoMenu.clicked.connect(self.MenuClieked)

        self.pushButton_GoBaseMakeup = QtWidgets.QPushButton(self)
        self.pushButton_GoBaseMakeup.setObjectName("pushButton_GoBaseMakeup")
        self.pushButton_GoBaseMakeup.setMinimumHeight(220)
        self.pushButton_GoBaseMakeup.setStyleSheet("border-image: url(image/menu_btn_base_makeup.png);")
        self.pushButton_GoBaseMakeup.clicked.connect(self.BaseMakeupClieked)

        self.pushButton_GoPersonalColor = QtWidgets.QPushButton(self)
        self.pushButton_GoPersonalColor.setObjectName("pushButton_GoPersonalColor")
        self.pushButton_GoPersonalColor.setMinimumHeight(220)
        self.pushButton_GoPersonalColor.setStyleSheet("border-image: url(image/menu_btn_personal_color.png);")
        self.pushButton_GoPersonalColor.clicked.connect(self.PersonalColorClieked)

        self.pushButton_GoCapture = QtWidgets.QPushButton(self)
        self.pushButton_GoCapture.setObjectName("pushButton_GoCapture")
        self.pushButton_GoCapture.setMinimumHeight(220)
        self.pushButton_GoCapture.setStyleSheet("border-image: url(image/menu_btn_capture.png);")
        self.pushButton_GoCapture.clicked.connect(self.CaptureClieked)

        self.pushButton_GoSelect = QtWidgets.QPushButton(self)
        self.pushButton_GoSelect.setObjectName("pushButton_GoSelect")
        self.pushButton_GoSelect.setMinimumHeight(220)
        self.pushButton_GoSelect.setStyleSheet("border-image: url(image/menu_btn_select.png);")
        self.pushButton_GoSelect.clicked.connect(self.SelectClieked)

        self.pushButton_GoExit = QtWidgets.QPushButton(self)
        self.pushButton_GoExit.setObjectName("pushButton_GoExit")
        self.pushButton_GoExit.setMinimumSize(160, 75)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton_GoExit.setFont(font)
        self.pushButton_GoExit.setText("EXIT")
        self.pushButton_GoExit.setStyleSheet("color: white;"
                                             "background-color: #5B5B5B")
        self.pushButton_GoExit.clicked.connect(self.ExitClieked)

        ## 레이아웃 배치
        titlebar = QHBoxLayout()
        titlebar.setContentsMargins(0, 0, 0, 0)
        titlebar.addWidget(self.label_titlebar)

        gbox = QGridLayout()
        gbox.setContentsMargins(0, 0, 0, 10)
        gbox.addWidget(self.pushButton_GoHome, 0, 0,)
        gbox.addWidget(self.pushButton_GoMenu, 0, 1)
        gbox.addWidget(self.pushButton_GoBaseMakeup, 0, 2)
        gbox.addWidget(self.pushButton_GoPersonalColor, 1, 0)
        gbox.addWidget(self.pushButton_GoCapture, 1, 1)
        gbox.addWidget(self.pushButton_GoSelect, 1, 2)
        gbox.addWidget(self.pushButton_GoExit, 2, 2, Qt.AlignCenter)


        layout.addLayout(titlebar)
        layout.addLayout(gbox)

        self.setLayout(layout)

    def showModal(self):  # 새 Modal 창이 열렸을 경우 기존에 있던 창을 사용하지 못하는 방식입니다.
        return super().exec_()

    def CloseClieked(self):
        self.reject()

    def HomeClieked(self):
        print("home clicked")
        self.btn = 1
        self.accept()

    def MenuClieked(self):
        print("main menu clicked")
        self.btn = 2
        self.accept()

    def BaseMakeupClieked(self):
        print("base makeup video clicked")
        self.btn = 3
        self.accept()

    def PersonalColorClieked(self):
        print("personal color clicked")
        self.btn = 4
        self.accept()

    def CaptureClieked(self):
        print("color makeup clicked")
        self.btn = 5
        self.accept()

    def SelectClieked(self):
        print("sub menu clicked")
        self.btn = 6
        self.accept()

    def ExitClieked(self):
        print("exit clicked")
        self.btn = 0
        self.accept()