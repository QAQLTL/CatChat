from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from model import *

class QInformaWidget(QPopupWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.personal_avatar = QAvatarWidget(self)
        self.personal_name = QLabel(self)
        self.personal_ipv4 = QLabel(self)

        self.personal_hlayout = QHBoxLayout()
        self.personal_right_vlayout = QVBoxLayout()
        self.vlayout = QVBoxLayout()

        self.ui_init()

    def ui_init(self):
        if self.parent:
            parent_pos = self.parent.mapToGlobal(QPoint(0, 0))
            self.move(parent_pos.x() + self.parent.width() + 15, parent_pos.y() - 10)

        self.personal_name.setObjectName("Name")
        self.personal_ipv4.setObjectName("Ipv4")
        self.personal_avatar.setFixedSize(QSize(60, 60))

        self.personal_hlayout.addWidget(self.personal_avatar)
        self.personal_right_vlayout.addWidget(self.personal_name, alignment=Qt.AlignmentFlag.AlignCenter)
        self.personal_right_vlayout.addWidget(self.personal_ipv4, alignment=Qt.AlignmentFlag.AlignCenter)
        self.personal_hlayout.addLayout(self.personal_right_vlayout)
        self.personal_right_vlayout.setContentsMargins(0, 10, 0, 10)

        self.vlayout.addLayout(self.personal_hlayout)

        self.setLayout(self.vlayout)
        self.style()

    def style(self):
        self.personal_name.setStyleSheet("""
        #Name {
            font-family: Arial Black;
            font-size: 20px;
            color: #1E2022;
        }
        """)
        self.personal_ipv4.setStyleSheet("""
        #Ipv4 {
            font-size: 10px;
            color: #52616B;
        }
        """)



