import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QApplication, QMainWindow
from Button4 import button4

class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        super().__init__()
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

        member.clicked(self.onButtonClicked)
        self.resize(200, 200)
        self.move(300, 300)
        self.setWindowTitle('스타벅스')
        self.show()



    def onButtonClicked(self):
        win =

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "주문을 취소하시겠습니까",
                                     QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close_say_hello()
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    FirstWindow = FirstWindow()
    FirstWindow.show()
    sys.exit(app.exec_())