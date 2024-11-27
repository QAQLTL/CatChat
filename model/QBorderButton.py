from PyQt6 import QtWidgets, QtCore, QtGui

class QBorderButton(QtWidgets.QPushButton):
    def __init__(self, parent=None, name:str=None):
        super().__init__(parent=parent)
        self.__name = name
        self.ui_init()


    def ui_init(self):
        self.setObjectName("QBorderButton")
        self.setStyleSheet("""
        #QBorderButton {
            padding: 5px;
            font-size: 11px;
            font-family: Arial Black;
            color: #73624D;
            border: 1px solid #73624D;
            border-radius: 13px;
        }
        """)

        self.setText(self.__name)

