from PyQt6.QtGui import QColor
from PyQt6 import QtCore
from PyQt6.QtWidgets import QGraphicsDropShadowEffect, QVBoxLayout
from qframelesswindow import StandardTitleBar

from model import QFullinformation, QFramelessmeun
from view import MainFrame

class MainV(MainFrame):
    def __init__(self):
        super().__init__()
        self.setTitleBar(StandardTitleBar(self))
        self.fullinformat = QFullinformation(self)
        self.meun = QFramelessmeun(self)
        self.Leftlayout.addWidget(self.fullinformat)
        self.Leftlayout.addWidget(self.meun)
        self.__shadowinit()

    def __shadowinit(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setXOffset(4)
        shadow.setYOffset(6)
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.fullinformat.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setXOffset(3)
        shadow.setYOffset(4)
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.navigationbar.setGraphicsEffect(shadow)