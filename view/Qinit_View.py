from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from qframelesswindow import FramelessWindow

class QInitView(FramelessWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("QinitView")
        self.setFixedSize(500, 500)
        self.setStyleSheet("""
        #QinitView { background-color: #F0F5F9; }
        """)

        self.Vlayout = QVBoxLayout(self)
        self.Vlayout.setContentsMargins(0, 40, 0, 0)