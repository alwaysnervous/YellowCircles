import random
import sys

from math import cos, sin, pi
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint, QPointF
from PyQt5.QtWidgets import QWidget, QApplication


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.circle = False
        self.square = False
        self.triangle = False
        self.flag = False
        self.qp = QPainter()
        self.coords = 0, 0
        self.setMouseTracking(True)
        self.initUI()

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def initUI(self):
        self.setGeometry(0, 0, 1000, 1000)
        self.setWindowTitle('Супрематизм')

    def draw(self):
        x, y = self.coords
        random_number = random.randint(20, 100)
        rgb_r = random.randint(0, 255)
        rgb_g = random.randint(0, 255)
        rgb_b = random.randint(0, 255)
        color = QColor(rgb_r, rgb_g, rgb_b)
        self.qp.setBrush(color)

        if self.circle:
            self.qp.drawEllipse(int(x - random_number / 2), int(y - random_number / 2), random_number, random_number)
        elif self.square:
            self.qp.drawRect(int(x - random_number / 2), int(y - random_number / 2), random_number, random_number)
        elif self.triangle:
            # r = random_number
            # a = r * (3 ** 0.5)
            # x1, x2, x3 = x - a // 2, x, x + a // 2
            # y1, y2, y3 = y + r // 2, y - r, y + r // 2
            # qp.drawPolygon(QPointF(x1, y1), QPointF(x2, y2), QPointF(x3, y3))
            coords = [QPoint(x, y - random_number),
                      QPoint(int(x + cos(7 * pi / 6) * random_number),
                             int(y - sin(7 * pi / 6) * random_number)),
                      QPoint(int(x + cos(11 * pi / 6) * random_number),
                             int(y - sin(11 * pi / 6) * random_number))]
            self.qp.drawPolygon(*coords)

        self.circle = False
        self.square = False
        self.triangle = False

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.triangle = True
        self.drawf()

    def mouseMoveEvent(self, event):
        self.coords = event.x(), event.y()

    def mousePressEvent(self, event):
        self.coords = event.x(), event.y()
        if event.button() == Qt.LeftButton:
            self.circle = True
        elif event.button() == Qt.RightButton:
            self.square = True
        self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
