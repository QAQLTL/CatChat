import sys

from PyQt6.QtWidgets import QApplication

from controller import MainV

class Window(MainV):
    def __init__(self):
        super().__init__()
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()

