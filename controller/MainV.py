from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from model import *
from common import *
from view import MainFrame

ip = IPclass()
settings = Config("Personal")

class MainV(MainFrame):
    def __init__(self):
        super().__init__()
        self.personal_avatar = QAvatarWidget(self)
        self.linespace = QFrame(self)
        self.usermenu = QUserMeun()

        self.__avatar_path = settings.load_avatar_path()
        self.__personal_name = settings.load_username()
        self.__personal_ipv4 = settings.load_useripv4() or ip.curripv4

        self.ui_init()

    def ui_init(self):
        self.titleBar.hide()
        self.setMinimumSize(0, 300)
        self.setMaximumSize(0, 445)

        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.personal_avatar.setimage(self.__avatar_path)
        self.personal_avatar.setFixedSize(QSize(60, 60))
        self.personal_avatar.clicked.connect(self.personal_avatar_event)

        self.linespace.setFrameShape(QFrame.Shape.HLine)
        self.linespace.setFrameShadow(QFrame.Shadow.Raised)

        self.VLayout.addWidget(self.personal_avatar, 0, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        self.VLayout.addWidget(self.linespace, 1)
        self.VLayout.addWidget(self.usermenu, 1)

        self.style()

    def style(self):
        pass

    def personal_avatar_event(self):
        if hasattr(self, "personal_widget") and self.personal_widget.isVisible():
            self.personal_widget.hide()
            return

        self.personal_widget = QInformaWidget(self.personal_avatar)
        self.personal_widget.personal_avatar.setimage(self.__avatar_path)
        self.personal_widget.personal_name.setText(self.__personal_name)
        self.personal_widget.personal_ipv4.setText(self.__personal_ipv4)

        self.personal_widget.show()