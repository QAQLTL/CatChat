from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QLabel, QLineEdit, QHBoxLayout


class QLineLabel(QLabel):
    def __init__(self, parent=None, text:str=None):
        super().__init__(parent=parent)
        self.setText(text)
        self.ui_init()

    def ui_init(self):
        self.setFixedHeight(25)
        self.setStyleSheet("""
        QLabel {
           font-family: Arial Black;
           font-size: 22px;
           background-color: transparent;
           border-radius: 0px;
           padding: 2px;
           border-bottom: 2px solid #A7A7A7;
           color: #4E4E4E;
        }
        """)