from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QLabel, QLineEdit, QHBoxLayout

class QLineEditBar(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui_init()

    def ui_init(self):
        self.setStyleSheet("""
        QLineEdit {
           font-size: 13px;
           background-color: #F2F2F2;
           border-radius: 11px;
           padding: 5px 5px 5px 8px;
           border: 1px solid #73624D;
           color: #73624D;
        }
        """)

        self.setPlaceholderText("UUID")