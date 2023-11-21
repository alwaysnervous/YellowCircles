import io
import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication


class Interface:
    def __init__(self):
        self.ui = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="0" column="0">
     <widget class="QPushButton" name="pushButton">
      <property name="text">
       <string>Кнопка</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>19</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = Interface()
        ui = io.StringIO(ui.ui)
        loadUi(ui, self)
        self.circle = False
        self.square = False
        self.triangle = False
        self.flag = False
        self.qp = QPainter()
        self.initui()

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def initui(self):
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.circle = True
        self.drawf()
        pass

    def draw(self):
        x, y = random.randint(0, 800), random.randint(0, 600)
        random_number = random.randint(20, 100)
        rgb_r = random.randint(0, 255)
        rgb_g = random.randint(0, 255)
        rgb_b = random.randint(0, 255)
        color = QColor(rgb_r, rgb_g, rgb_b)
        self.qp.setBrush(color)

        if self.circle:
            self.qp.drawEllipse(int(x - random_number / 2), int(y - random_number / 2), random_number, random_number)

        self.circle = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
