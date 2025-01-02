from PyQt6.QtCore import *
from PyQt6.QtWidgets import QLabel, QLineEdit, QHBoxLayout


class QLineEditBar(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.animation = None
        self.target_width = 150
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

    def start_animation(self):
        self.animate_width(self.width(), self.target_width)

    def end_animation(self):
        if self.animation:
            self.animation.stop()

        self.animate_width(self.width(), 0)

    def animate_width(self, start_width, end_width):
        if self.animation:
            self.animation.stop()

        self.animation = QPropertyAnimation(self, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(start_width)
        self.animation.setEndValue(end_width)
        self.animation.start()