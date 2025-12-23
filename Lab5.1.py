import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(400, 400)

    def paintEvent(self, e):
        painter = QPainter(self)
        self.draw_shape(painter)
        painter.end()

    def draw_shape(self, painter):
        pass

class Simple_drawing_window1(Simple_drawing_window):
    def __init__(self):
        super().__init__("1")

    def draw_shape(self, p):
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(255, 0, 0))
        p.drawRect(50, 50, 150, 100)

def main():
    app = QApplication(sys.argv)

    w1 = Simple_drawing_window1()
    #w2 = Simple_drawing_window2()
    #w3 = Simple_drawing_window3()

    w1.show()
    #w2.show()
    #w3.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()