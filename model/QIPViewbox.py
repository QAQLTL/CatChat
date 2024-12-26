from msilib.schema import SelfReg

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from common import IPclass

ip = IPclass()


class QIPViewbox(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hlayout = QHBoxLayout(self)
        self.netcheck = NetCheck(self)
        self.ipbutton = IPbutton(self)

        self.timer = QTimer(self)
        self.test_result = None
        self.ui_init()

    def ui_init(self):
        self.setFixedHeight(32)
        self.setFixedWidth(200)
        self.setContentsMargins(8, 0, 5, 0)
        self.hlayout.addWidget(self.netcheck, 1)
        self.hlayout.addWidget(self.ipbutton, 1)

        self.timer.timeout.connect(self.refresh_check_net)
        self.timer.start(0)

    def refresh_check_net(self):
        ip.getcurrip()
        ipv4 = ip.curripv4
        if ipv4 == "127.0.0.1":
            self.test_result = False
        elif ipv4 != "127.0.0.1":
            self.test_result = True
        else:
            self.test_result = None
        self.netcheck.set_result(self.test_result)
        self.ipbutton.refresh_ip(ipv4)

class IPbutton(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("IPLabel")
        self.setText(f"{ip.curripv4}")

        self.ui_init()

    def ui_init(self):
        pass

    def refresh_ip(self, context):
        self.setText(f"{context}")

class IPMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("IPmenu")

        self.ui_init()

    def ui_init(self):
        pass

class NetCheck(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.test_result = None
        self.color = "gray"
        self.setObjectName("NetCheckLabel")
        self.ui_init()

    def ui_init(self):
        # 设置固定尺寸并初始化样式
        self.setFixedSize(15, 15)
        self.update_style()

    def update_style(self):
        # 更新 QLabel 的样式
        self.setStyleSheet(
            f"""
            background-color: {self.color};
            border-radius: 7px;
            """
        )

    def set_result(self, result):
        """设置测试结果并更新颜色"""
        self.test_result = result
        if self.test_result is None:
            self.color = "gray"
        elif self.test_result:
            self.color = "#64ED69"
        else:
            self.color = "#EF5F58"
        self.update_style()