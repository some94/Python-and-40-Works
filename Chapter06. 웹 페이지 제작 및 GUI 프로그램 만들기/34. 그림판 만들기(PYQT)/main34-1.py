import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


ui_path = r"C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter06. 웹 페이지 제작 및 GUI 프로그램 만들기\34. 그림판 만들기(PYQT)\그림판.ui"
form_class = uic.loadUiType(ui_path)[0]


class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()