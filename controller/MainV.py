from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from qframelesswindow import StandardTitleBar

from model import QFullinformation, QFramelessmenu, QIPViewbox, QBorderButton
from view import MainFrame, QAddView

class MainV(MainFrame):
    def __init__(self):
        super().__init__()
        self.setTitleBar(StandardTitleBar(self))
        self.ipviewbox = QIPViewbox(self)
        self.fullinformat = QFullinformation(self)
        self.meun = QFramelessmenu(parent=self, title="Chat")
        self.settingbut = QBorderButton(self, sizeh=18, sizew=18)

        self.add_view = QAddView()

        self.ui_init()

    def ui_init(self):
        parent_geometry = self.geometry()
        child_x = parent_geometry.x() / 0.9
        child_y = parent_geometry.y() / 0.9
        self.titleBar.maxBtn.deleteLater()
        self.titleBar._isDoubleClickEnabled = False

        self.meun.setmeun_action(self.add_view)
        self.add_view.move(child_x, child_y)

        self.settingbut.seticon(iconpath="D:/python/CatChat/res/settings.png")
        self.settingbut.setStyleSheet("""
        #QBorderButton {
            font-size: 18px;
            font-family: Arial Black;
            background-color: transparent;
        }
        """)

        self.Leftlayout.addWidget(self.fullinformat, 0)
        self.Leftlayout.addWidget(self.meun, 0)
        self.buttomlayout.addWidget(self.ipviewbox, 0, alignment=Qt.AlignmentFlag.AlignRight)
        self.buttomlayout.addWidget(self.settingbut, 0, alignment=Qt.AlignmentFlag.AlignRight)

        self.shadow_inforbox()

    def shadow_inforbox(self):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QColor('#222222'))
        shadow.setOffset(0, 0)

        self.fullinformat.setGraphicsEffect(shadow)

    def closeEvent(self, a0):
        self.add_view.close()