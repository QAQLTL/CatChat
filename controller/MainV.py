from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QGraphicsDropShadowEffect, QVBoxLayout
from qframelesswindow import StandardTitleBar

from model import QFullinformation, QFramelessmenu
from view import MainFrame

class MainV(MainFrame):
    def __init__(self):
        super().__init__()
        self.setTitleBar(StandardTitleBar(self))
        self.fullinformat = QFullinformation(self)
        self.meun = QFramelessmenu(parent=self, title="Strange Zone")
        self.Leftlayout.addWidget(self.fullinformat)
        self.Leftlayout.addWidget(self.meun)
        self.__shadowinit()

    def __shadowinit(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setXOffset(3)
        shadow.setYOffset(4)
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.navigationbar.setGraphicsEffect(shadow)