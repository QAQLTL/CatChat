from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from model import *
from common import *

network = NetCatCHAT()
settings = Config("Personal")
dataManager = FriendManager(f"{os.getcwd()}/data/JsonData/userdata.json")
dataManager.load_from_json()

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
        self.add_user.clicked.connect(self.addwidget_event)

    def addwidget_event(self):
        if hasattr(self, "addwin") and self.addwin.isVisible():
            self.addwin.hide()
            return

        self.addwin = AddUserWindow(self.add_user)

        self.addwin.window_opened.connect(network.start_listen)
        self.addwin.window_closed.connect(network.stop_listen)
        self.addwin.show()
        network.devices_updated.connect(self.addwin.update_items)

class CustomWidget(BaseCustomWidget):
    def __init__(self, parent=None, image_path:str = None):
        super().__init__(parent)
        self.avatar = QAvatarWidget(self.widget)
        self.image_path = image_path

        self.ui_init()

    def ui_init(self):
        self.avatar.setFixedSize(QSize(60, 60))
        if self.image_path:
            self.avatar.setimage(self.image_path)
        self.layout.addWidget(self.avatar)
        self.avatar.clicked.connect(self._on_pressed)

    def _on_pressed(self):
        self.chat_widget = ChatWindow()
        self.chat_widget.show()

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
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        item = CustomAddWidget(self.user_list_view)
        self.user_list_view.setItemWidget(item, item.widget)

        for friend in dataManager.friends:
            avatar_path = friend.get("avatar_path", "")

            item = CustomWidget(self.user_list_view, avatar_path)
            self.user_list_view.setItemWidget(item, item.widget)

        self.vlayout.setSpacing(0)
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.addWidget(self.user_list_view, 1)

    def showEvent(self, event):
        """窗口顯示事件，發送 `window_opened` 信號。"""
        super().showEvent(event)
        network.update_name(settings.load_username())
        network.start_broadcast()
