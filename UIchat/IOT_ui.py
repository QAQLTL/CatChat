from PyQt6.QtWidgets import QWidget
from IOTui import Ui_IOT_UI

class IOTInterface(QWidget, Ui_IOT_UI):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)