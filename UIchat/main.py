import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from IOT_ui import IOTInterface
from qfluentwidgets import SplitFluentWindow, FluentIcon

class Mwin(SplitFluentWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SocChat")
        self.io = IOTInterface(self)
        self.addSubInterface(self.io, FluentIcon.IOT, "IOT")

if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # QApplication.setAttribute(Qt.AA_UseHighDpoPixmaps)

    app = QApplication(sys.argv)
    mw = Mwin()
    mw.show()
    app.exec()

