from PyQt6 import QtWidgets, QtCore, QtGui

class QBorderButton(QtWidgets.QPushButton):
    def __init__(self, parent=None, name:str=None, sizew:int=None, sizeh:int=None):
        super().__init__(parent=parent)
        self.__sizew = sizew
        self.__sizeh = sizeh
        self.__name = name
        self.ui_init()


    def ui_init(self):
        self.setObjectName("QBorderButton")
        self.setStyleSheet("""
        #QBorderButton {
            padding: 5px;
            font-size: 18px;
            font-family: Arial Black;
            background-color: #52616B;
            border-radius: 10px;
            color: #F0F5F9;
        }
        """)
        self.setText(self.__name)

    def seticon(self, iconpath):
        self.setIcon(QtGui.QIcon(iconpath))
        self.setIconSize(QtCore.QSize(self.__sizew, self.__sizeh))
