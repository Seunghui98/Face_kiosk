import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QApplication, QMainWindow
from SubWindow import SubWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('Star Bucks Kiosk')

        layout = QVBoxLayout()
        layout.addStretch(1)

        self.setFixedSize(600, 900)
        oImage = QImage("image/back1.png")
        sImage = oImage.scaled(QSize(600, 900))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)
        m = QIcon("image/m.png")
        nm = QIcon("image/nm.png")

        member = QPushButton(m, "", self)
        member.setIconSize(QSize(400, 100))
        member.move(100, 300)

        non_member = QPushButton(nm, "", self)
        non_member.setIconSize(QSize(400, 100))
        non_member.move(100, 500)

        member.clicked.connect(self.onButtonClicked)

        self.resize(200, 200)
        self.move(300, 300)
        self.show()



    def onButtonClicked(self):
        self.close()
        win = SubWindow()

        r = win.showModal()

    def show(self):
        super().show()





