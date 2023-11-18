import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QGridLayout, QMenuBar, QStatusBar
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import *
from random import randint


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 400)
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for circle in self.circles:
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 598)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(4, 530, 791, 23))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 781, 511))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 802, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\
\u0442\u044c \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u044c", None))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.circle_widget = CircleWidget()
        self.gridLayout.addWidget(self.circle_widget)
        self.pushButton.clicked.connect(self.circle_widget.add_circle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())