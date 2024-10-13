import sys
from PyQt6.QtWidgets import QApplication
from left_ui import Window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()

