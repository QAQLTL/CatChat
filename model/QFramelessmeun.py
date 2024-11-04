from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QPushButton

class __Struct:
    def __int__(self, name:str=None, avatar:str=None, ipv4:str=None, ipv6:str=None):
        self.__name = name
        self.__avatar = avatar
        self.__ipv4 = ipv4
        self.__ipv6 = ipv6

class QFramelessmeun(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__list = []

        # set button
        self.setStyleSheet("""{border-radius: 20px; border: 1px solid #E0E0E0}""")
        self.__meunbutton = QPushButton(self)
        self.ui_init()

    def ui_init(self):
        self.__meunbutton.setFlat(True)
        self.__meunbutton.setText("Client")

    def add(self):
        pass

    def getlen(self) -> int:
        return len(self.__list)
