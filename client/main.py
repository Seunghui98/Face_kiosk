import sys
from MainWindow import MainWindow
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


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

