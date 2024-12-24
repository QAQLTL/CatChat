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
           background-color: #F0F5F9;
           border-radius: 11px;
           padding: 5px 5px 5px 8px;
           border: 2px solid #52616B;
           color: #73624D;
        }
        """)