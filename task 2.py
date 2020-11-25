import sys
from random import randrange
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, uic


class App(QtWidgets.QWidget):
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
        painter.setBrush(QColor(randrange(0, 255), randrange(0, 255), randrange(0, 255)))
        r = randrange(10, self.width() // 5)
        painter.drawEllipse(self.x - r, self.y - r, 2 * r, 2 * r)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exit(app.exec())
