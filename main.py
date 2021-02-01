import sys
from random import randrange
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, uic
import sys
from PyQt5 import QtWidgets
import UI


class Circle(QtWidgets.QWidget, UI.Ui_Form):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.x = 250
        self.y = 250
        self.build_handlers()

    def build_handlers(self):
        self.pushButton.clicked.connect(self.repaint)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.circle(painter)
        painter.end()

    def circle(self, painter):
        painter.setBrush(QColor('yellow'))
        r = randrange(10, self.width() // 5)
        painter.drawEllipse(self.x - r, self.y - r, 2 * r, 2 * r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def main():
    app = QtWidgets.QApplication(sys.argv)
    start_window = Circle()
    start_window.show()
    sys.excepthook = except_hook
    app.exec_()


if __name__ == "__main__":
    main()
