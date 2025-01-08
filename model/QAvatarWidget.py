from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from .QCircleimage import QCircleimage

class QAvatarWidget(QCircleimage, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui_init()

    def ui_init(self):
        self.setFixedSize(QSize(60, 60))

        self.style()

    def style(self):
        self.setStyleSheet("""
        background-color: transparent;
        """)