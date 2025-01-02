from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from model import QCircleimage, QCircleAddUser


class BaseCustomWidget(QListWidgetItem):
    def __init__(self, parent=None, size: QSize = QSize(60, 60)):
        super().__init__(parent)
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setSizeHint(size)

    def get_widget(self):
        return self.widget


class CustomAddWidget(BaseCustomWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.add_user = QCircleAddUser(self.widget)
        self.layout.addWidget(self.add_user)
        self.ui_init()

    def ui_init(self):
        pass


class CustomWidget(BaseCustomWidget):
    def __init__(self, parent=None, image_path: str = None):
        super().__init__(parent)
        self.avatar = QCircleimage(self.widget)
        self.avatar.setFixedSize(QSize(60, 60))
        if image_path:
            self.avatar.setimage(image_path)
        self.layout.addWidget(self.avatar)


class QUserlistview(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui_init()

    def ui_init(self):
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.setSpacing(5)
        self.setObjectName("ListW")
        self.setStyleSheet("""
        #ListW {
            background-color: transparent;
            border: none;
            outline: 0px;
        }
        QListWidget::item {
            background-color: transparent;
            border: none;
        }
        QListWidget::item:selected {
            background-color: transparent;
            color: inherit;
        }
        """)


class QUserMeun(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vlayout = QVBoxLayout(self)
        self.user_list_view = QUserlistview(self)
        self.ui_init()

    def ui_init(self):
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        item = CustomAddWidget(self.user_list_view)
        self.user_list_view.setItemWidget(item, item.widget)

        for i in range(0, 4):
            item = CustomWidget(self.user_list_view, "D:/python/CatChat/res/cc.png")
            self.user_list_view.setItemWidget(item, item.widget)

        self.vlayout.setSpacing(0)
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.addWidget(self.user_list_view, 1)

    def style(self):
        self.setStyleSheet("""
        """)