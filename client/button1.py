import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon


def __init__(self):
    super().__init__()

    self.creat_connect()
    self.init_ui()


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle('카페')
    win.setGeometry(200, 200, 220, 100)
    win.setWindowIcon(QIcon('mesaj.png'))

    lblAd = QtWidgets.QLabel(win)
    lblAd.setText("회원")
    lblAd.move(20, 10)

    lblSoyad = QtWidgets.QLabel(win)
    lblSoyad.setText("비회원")
    lblSoyad.move(20, 35)

    tbKuladi = QtWidgets.QLineEdit(win)
    tbKuladi.setMaximumHeight(20)
    tbKuladi.move(100, 15)

    tbSifre = QtWidgets.QLineEdit(win)
    tbSifre.setMaximumHeight(20)
    tbSifre.move(100, 40)

    def tikla(self):
        print("Kullanıcı adı : " + tbKuladi.text())
        print("Şifre : " + tbSifre.text())

    btnGiris = QtWidgets.QPushButton(win)
    btnGiris.setText("검색")
    btnGiris.move(100, 65)
    btnGiris.clicked.connect(tikla)

    win.setToolTip('Üstüme geldin')
    win.show()
    sys.exit(app.exec_())


window()