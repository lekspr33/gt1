import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
import random


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paintEvent)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircle(qp)
        qp.end()

    def drawCircle(self, qp):
        diameter = random.randint(10, 100)
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, diameter, diameter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
