from qframelesswindow import StandardTitleBar

from model import QFullinformation, QFramelessmenu, QChatW
from view import MainFrame, QAddView

class MainV(MainFrame):
    def __init__(self):
        super().__init__()
        self.setTitleBar(StandardTitleBar(self))
        self.fullinformat = QFullinformation(self)
        self.meun = QFramelessmenu(parent=self, title="Chat Zone")

        self.add_view = QAddView()

        self.ui_init()

    def ui_init(self):
        parent_geometry = self.geometry()
        child_x = parent_geometry.x() / 0.9
        child_y = parent_geometry.y() / 0.9
        self.titleBar.maxBtn.deleteLater()  # 移除最大化按钮
        self.titleBar._isDoubleClickEnabled = False  # 禁用双击放大

        self.meun.setmeun_action(self.add_view)
        self.add_view.move(child_x, child_y)

        self.Leftlayout.addWidget(self.fullinformat)
        self.Leftlayout.addWidget(self.meun)

    def closeEvent(self, a0):
        self.add_view.close()