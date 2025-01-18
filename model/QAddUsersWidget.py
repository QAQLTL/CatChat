from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from .QSearch import SearchApp

from .QPopupWidget import QPopupWidget
from common import *

config = Config("Personal")

class AddUserWindow(QPopupWidget):
    window_closed = pyqtSignal()
    window_opened = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.items = []
        self.searchbar = SearchApp()
        self.list_widget = QListWidget()
        self.vlayout = QVBoxLayout(self)
        self.list_widget.currentItemChanged.connect(self.on_item_changed)

        self.ui_init()

    def ui_init(self):
        self.setFixedSize(300, 300)

        if self.parent:
            parent_pos = self.parent.mapToGlobal(QPoint(0, 0))
            self.move(parent_pos.x() + self.parent.width() + 15, parent_pos.y() - 10)

        self.list_widget.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.vlayout.addWidget(self.searchbar, alignment=Qt.AlignmentFlag.AlignTop)
        self.vlayout.addWidget(self.list_widget, alignment=Qt.AlignmentFlag.AlignBottom)


        self.searchbar.search_bar.textChanged.connect(self.update_list)
        self.apply_list_widget_style()

    def on_item_changed(self, current, previous):
        if current:
            selected_username = current.text()
            selected_item = next((item for item in self.items if item["username"] == selected_username), None)
            if selected_item:
                request = FriendRequestSender(config.load_username(), config.load_avatar_path()).create_request()
                TCPClient(selected_item['ip']).send_message(request)
            else:
                print(f"找不到 {selected_username} 的完整資料")

    def update_list(self):
        """更新列表，根據搜尋文字過濾和排序。"""
        search_text = self.searchbar.search_bar.text().strip()
        self.list_widget.clear()

        if search_text:

            filtered_items = [
                item for item in self.items if search_text.lower() in item["username"].lower()
            ]


            sorted_filtered_items = sorted(
                filtered_items,
                key=lambda x: x["username"].lower().index(search_text.lower())
            )

            self.list_widget.addItems([item["username"] for item in sorted_filtered_items])
        else:
            self.list_widget.addItems([item["username"] for item in self.items])

    def update_items(self, items):
        """更新項目列表並刷新顯示。"""
        self.items = items
        self.update_list()

    def apply_list_widget_style(self):
        """設定 QListWidget 的樣式表。"""
        self.list_widget.setStyleSheet("""
            QListWidget {
                border: 1px solid #D6D6D6;
                border-radius: 5px;
                padding: 5px;
                background-color: #FFFFFF;
                font-family: Arial, sans-serif;
                font-size: 14px;
            }

            QListWidget::item {
                padding: 8px 10px;
                margin: 2px;
                border: 1px solid transparent;
                border-radius: 5px;
                background-color: #F9F9F9;
                color: #333333;
            }

            QListWidget::item:hover {
                background-color: #E6F7FF;
                border: 1px solid #91D5FF;
            }

            QListWidget::item:selected {
                background-color: #1890FF;
                border: 1px solid #0050B3;
                color: #FFFFFF;
            }

            QListWidget::item:selected:hover {
                background-color: #40A9FF;
                border: 1px solid #1890FF;
            }
        """)

    def showEvent(self, event):
        """窗口顯示事件，發送 `window_opened` 信號。"""
        super().showEvent(event)
        self.window_opened.emit()

    def closeEvent(self, event):
        """窗口關閉事件，發送 `window_closed` 信號。"""
        super().closeEvent(event)
        self.window_closed.emit()