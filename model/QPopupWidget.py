from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from qframelesswindow import FramelessWindow

class QPopupWidget(FramelessWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__timer = QTimer(self)
        self.__timer.setInterval(700)
        self.__timer.timeout.connect(self.start_close_animation)
        self.__timer.start()

        self.eventinit()

    def eventinit(self):
        self.titleBar.hide()
        self.setObjectName("PopupWidget")
        self.setStyleSheet("#PopupWidget { background-color: #F0F5F9; border-radius: 10px; }")

        self.setFixedSize(200, 80)
        self.setMaximumSize(200, 200)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.show_animation = QPropertyAnimation(self, b"windowOpacity")
        self.show_animation.setDuration(300)
        self.show_animation.setStartValue(0.0)
        self.show_animation.setEndValue(1.0)
        self.show_animation.start()

        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(300)
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.finished.connect(self.close)

    def leaveEvent(self, event):
        self.__timer.start()
        super().leaveEvent(event)

    def enterEvent(self, event):
        if self.__timer.isActive():
            self.__timer.stop()
        super().enterEvent(event)

    def start_close_animation(self):
        self.animation.start()
