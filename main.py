import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from random import randint
from PyQt5 import uic


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 400)
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for circle in self.circles:
            color = QColor(Qt.yellow)
            diameter = circle[0]
            x = circle[1] - diameter / 2
            y = circle[2] - diameter / 2

            painter.setPen(Qt.NoPen)
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)

    def add_circle(self):
        diameter = randint(10, 100)
        x = randint(diameter, self.width() - diameter)
        y = randint(diameter, self.height() - diameter)
        self.circles.append([diameter, x, y])
        self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.circle_widget = CircleWidget()

        self.gridLayout.addWidget(self.circle_widget)

        self.pushButton.clicked.connect(self.circle_widget.add_circle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())