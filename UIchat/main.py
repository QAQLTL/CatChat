import sys
from PyQt6 import QtWidgets, uic

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    hb_window = uic.loadUi("uichat.ui")
    hb_window.show()

    app.exec()