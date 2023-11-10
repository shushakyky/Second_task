from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.uic import loadUi
import random
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('UI.ui', self)
        self.button.clicked.connect(self.show_circle)
        self.diameters = []

    def show_circle(self):
        diameter = random.randint(10, 100)
        self.diameters.append(diameter)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QColor('yellow'))
        for diameter in self.diameters:
            painter.drawEllipse(self.width() // 2 - diameter // 2, self.height() // 2 - diameter // 2, diameter,
                                diameter)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())