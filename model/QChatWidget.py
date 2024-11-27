from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QVBoxLayout, QWidget

from .QLineEditBar import QLineEditBar

class QChatWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__Vlayout = QVBoxLayout(self)
        self.__ChatWidget = QWidget()
        self.__ChatInput = QLineEditBar()

        self.ui_init()

    def ui_init(self):
        self.__Vlayout.addWidget(self.__ChatWidget)
        self.__Vlayout.addWidget(self.__ChatInput)