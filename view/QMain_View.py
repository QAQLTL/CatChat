from PyQt6 import QtCore, QtGui, QtWidgets
from qframelesswindow import FramelessWindow


class MainFrame(FramelessWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("MainUI")
        self.resize(1200, 700)
        # self.setFixedSize(1200, 700)
        # Set size policy and stylesheet in one step
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        self.setStyleSheet("#MainUI { background-color: rgb(242,242,242); }")

        # Main layout setup
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setContentsMargins(30, 45, 30, -1)
        self.verticalLayout_2.setSpacing(10)

        # VLayout setup with MainLayout and navigation layout
        self.VLayout = QtWidgets.QVBoxLayout()
        self.Leftlayout = QtWidgets.QVBoxLayout()
        self.MainLayout = QtWidgets.QHBoxLayout()
        self.MainLayout.addLayout(self.Leftlayout)
        self.VLayout.addLayout(self.MainLayout)

        # set LeftLayout
        self.Leftlayout.setSpacing(20)
        self.Leftlayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        # Add layouts to the main layout
        self.verticalLayout_2.addLayout(self.VLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtCore.QCoreApplication.translate("MainUI", "MainUI"))
