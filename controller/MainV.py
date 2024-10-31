from PyQt6.QtGui import QColor
from PyQt6 import QtCore
from PyQt6.QtWidgets import QGraphicsDropShadowEffect
from qframelesswindow import StandardTitleBar

from model import QHInformat
from view import MainFrame

class MainV(MainFrame):
    def __init__(self):
        super().__init__()
        self.setTitleBar(StandardTitleBar(self))
        self.Informat_QW = QHInformat(parent=self)
        self.MainLayout.addWidget(self.Informat_QW, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        self.navigationbarshadow()

    def navigationbarshadow(self):

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setXOffset(2)
        shadow.setYOffset(3)
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(0, 0, 0, 64))

        self.navigationbar.setGraphicsEffect(shadow)