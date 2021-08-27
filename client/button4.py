from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import QScrollArea, QFormLayout, QVBoxLayout, QLabel, QWidget

class Ten(QDialog):
    def __init__(self, parent=None):
        super(Ten, self).__init__(parent)

        self.title = "2019 스타벅스 연령별 인기음료"
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 300

        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon("IMG-20190622-WA0011.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        oImage = QImage("veg1.jpg")
        sImage = oImage.scaled(QSize(400, 300))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        fromLayout = QFormLayout()
        groupbox = QGroupBox("장바구니에 담기")

        label_list = ['카페 아메리카노', '카페 라떼', '자바 칩 프라푸치노', '자몽 허니 블랙 티', '스타벅스 돌체 라떼', ] ##10대
        button_list = []

        for i in range(len(label_list)):
            label_list[i] = QLabel(label_list[i])
            label_list[i].setFont(QtGui.QFont("Times", weight=QtGui.QFont.Normal))
            label_list[i].setStyleSheet("color:white")
            button_list.append(QPushButton("선택"))
            button_list[i].setFixedSize(QSize(120, 30))
            fromLayout.addRow(label_list[i], button_list[i])

        groupbox.setLayout(fromLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)

        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)

class Twenty(QDialog):
    def __init__(self, parent=None):
        super(Twenty, self).__init__(parent)

        self.title = "2019 스타벅스 연령별 인기음료"
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 300

        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon("IMG-20190622-WA0011.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        oImage = QImage("Non.jpg")
        sImage = oImage.scaled(QSize(400, 300))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        fromLayout = QFormLayout()
        groupbox = QGroupBox("장바구니에 담기")

        label_list =['카페 아메리카노', '카페 라떼', '자몽 허니 블랙 티', '돌체 콜드 블루', '콜드 브루', ] ##20대

        button_list = []

        for i in range(len(label_list)):
            label_list[i] = QLabel(label_list[i])
            label_list[i].setFont(QtGui.QFont("Times", weight=QtGui.QFont.Normal))
            label_list[i].setStyleSheet("color:white")
            button_list.append(QPushButton("선택"))
            button_list[i].setFixedSize(QSize(120, 30))
            fromLayout.addRow(label_list[i], button_list[i])

        groupbox.setLayout(fromLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)

        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)


class Thirty(QDialog):
    def __init__(self, parent=None):
        super(Thirty, self).__init__(parent)

        self.title = "2019 스타벅스 연령별 인기음료"
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 300

        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon("IMG-20190622-WA0011.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        oImage = QImage("snak.jpg")
        sImage = oImage.scaled(QSize(400, 300))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        fromLayout = QFormLayout()
        groupbox = QGroupBox("장바구니에 담기")

        label_list = ['1. 카페 아메리카노', '2. 카페 라떼','3. 돌체 콜드 브루', '4. 스타벅스 돌체 라뗴', '5. 디카페인 아메리카노'] ##30대
        button_list = []

        for i in range(len(label_list)):
            label_list[i] = QLabel(label_list[i])
            label_list[i].setFont(QtGui.QFont("Times", weight=QtGui.QFont.Normal))
            label_list[i].setStyleSheet("color:white")
            button_list.append(QPushButton("선택"))
            button_list[i].setFixedSize(QSize(120, 30))
            fromLayout.addRow(label_list[i], button_list[i])

        groupbox.setLayout(fromLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)

        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)


class Forty(QDialog):
    def __init__(self, parent=None):
        super(Forty, self).__init__(parent)

        self.title = "2019 스타벅스 연령별 인기음료"
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 300

        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon("IMG-20190622-WA0011.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        oImage = QImage("brew.jpg")
        sImage = oImage.scaled(QSize(400, 300))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        fromLayout = QFormLayout()
        groupbox = QGroupBox("장바구니에 담기")

        label_list = ['카페 아메리카노', '카페 라떼','디카페인 아메리카노', '오늘의 커피', '카라멜 마끼아또']
        button_list = []

        for i in range(len(label_list)):
            label_list[i] = QLabel(label_list[i])
            label_list[i].setFont(QtGui.QFont("Times", weight=QtGui.QFont.Normal))
            label_list[i].setStyleSheet("color:white")
            button_list.append(QPushButton('선택'))
            button_list[i].setFixedSize(QSize(120, 30))
            fromLayout.addRow(label_list[i], button_list[i])

        groupbox.setLayout(fromLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)

        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)

class Fifty(QDialog):
    def __init__(self, parent=None):
        super(Fifty, self).__init__(parent)

        self.title = "2019 스타벅스 연령별 인기음료"
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 300

        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon("IMG-20190622-WA0011.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        oImage = QImage("veg1.jpg")
        sImage = oImage.scaled(QSize(400, 300))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        fromLayout = QFormLayout()
        groupbox = QGroupBox("장바구니에 담기")

        label_list = ['카페 아메리카노', '카페 라떼', '디카페인 아메리카노', '오늘의 커피', '카라멜 마끼야', ] ##50대
        button_list = []

        for i in range(len(label_list)):
            label_list[i] = QLabel(label_list[i])
            label_list[i].setFont(QtGui.QFont("Times", weight=QtGui.QFont.Normal))
            label_list[i].setStyleSheet("color:white")
            button_list.append(QPushButton("Add"))
            button_list[i].setFixedSize(QSize(120, 30))
            fromLayout.addRow(label_list[i], button_list[i])

        groupbox.setLayout(fromLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)

        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "스타벅스"
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 300

        self.setWindowIcon(QtGui.QIcon("IMG-20190622-WA0011.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QHBoxLayout()
        self.label = QLabel("\t   연령대를 선택하세요.")
        self.label.setFont(QtGui.QFont("Times",20,weight=QtGui.QFont.Normal))
        self.label.setStyleSheet("color:white")
        self.label.setAlignment(QtCore.Qt.AlignTop)
        vbox.addWidget(self.label)

        oImage = QImage("background.jpg")
        sImage = oImage.scaled(QSize(400, 300))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.setLayout(vbox)
        self.UiComponents()

        self.dialog1 = Ten(self)
        self.dialog2 = Twenty(self)
        self.dialog3 = Thirty(self)
        self.dialog4 = Forty(self)
        self.dialog5 = Fifty(self)

    def button_clicked1(self):
        self.dialog1.show()

    def button_clicked2(self):
        self.dialog2.show()

    def button_clicked3(self):
        self.dialog3.show()

    def button_clicked4(self):
        self.dialog4.show()

    def button_clicked5(self):
        self.dialog5.show()

#메인 화면
    def UiComponents(self):
        button1 = QPushButton("10대", self)
        button1.setGeometry(QRect(50, 70, 120, 30))
        button1.setIcon(QtGui.QIcon("veg1.jpg"))
        button1.setIconSize(QSize(25, 25))
        button1.setToolTip("Explore varieties of 10대")

        button1.clicked.connect(self.button_clicked1)

        button2 = QPushButton("20대", self)
        button2.setGeometry(QRect(250, 70, 120, 30))
        button2.setIcon(QtGui.QIcon("Non veg.jpg"))
        button2.setIconSize(QSize(25, 25))
        button2.setToolTip("Explore varieties of 20대 ")

        button2.clicked.connect(self.button_clicked2)

        button3 = QPushButton("30대", self)
        button3.setGeometry(QRect(50, 170, 120, 30))
        button3.setIcon(QtGui.QIcon("snacks.jpg"))
        button3.setIconSize(QSize(25, 25))
        button3.setToolTip("Explore varieties of 30대 ")

        button3.clicked.connect(self.button_clicked3)

        button4 = QPushButton("40대", self)
        button4.setGeometry(QRect(250, 170, 120, 30))
        button4.setIcon(QtGui.QIcon("brew.jpg"))
        button4.setIconSize(QSize(25, 25))
        button4.setToolTip("Explore varieties of 40대 ")

        button4.clicked.connect(self.button_clicked4)

        button5 = QPushButton("50대 이상", self)
        button5.setGeometry(QRect(150, 250, 120, 30))
        button5.setIcon(QtGui.QIcon("whatever.jpg"))
        button5.setIconSize(QSize(25, 25))
        button5.setToolTip("Explore varieties of 50대이상 ")

        button5.clicked.connect(self.button_clicked5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())