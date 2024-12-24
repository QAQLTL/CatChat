from PyQt6 import QtCore, QtGui, QtWidgets
from qframelesswindow import FramelessWindow

class MainFrame(FramelessWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("MainUI")
        # self.setFixedSize(1200, 700)
        # Set size policy and stylesheet in one step
        self.setFixedSize(0, 696)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        self.setStyleSheet("#MainUI { background-color: #F0F5F9; }")

        # Main layout setup
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setContentsMargins(0, 40, 0, 0)
        self.verticalLayout_2.setSpacing(10)

        # VLayout setup with MainLayout and navigation layout
        self.VLayout = QtWidgets.QVBoxLayout()
        self.VLayout.setContentsMargins(25, 0, 25, 0)
        self.Leftlayout = QtWidgets.QVBoxLayout()
        self.VLayout.addLayout(self.Leftlayout)

        # set LeftLayout
        self.Leftlayout.setSpacing(5)
        self.Leftlayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        # Add layouts to the main layout
        self.verticalLayout_2.addLayout(self.VLayout)

        # set Buttom layout
        self.buttomlayout = QtWidgets.QHBoxLayout()
        self.buttomlayout.setContentsMargins(0,0,5,0)
        self.verticalLayout_2.addLayout(self.buttomlayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtCore.QCoreApplication.translate("MainUI", "MainUI"))
