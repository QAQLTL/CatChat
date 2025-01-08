from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from qframelesswindow import FramelessWindow

class ChatBubble(QWidget):
    def __init__(self, text, is_left=True, parent=None):
        super().__init__(parent)
        self.text = text
        self.is_left = is_left
        self._create_bubble()

    def _create_bubble(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)

        label = QLabel(self.text)
        label.setStyleSheet(
            """
            QLabel {
                background-color: #d1f7c4;  /* 氣泡背景顏色 */
                border: 1px solid #a9d08e; /* 氣泡邊框顏色 */
                border-radius: 15px;       /* 圓角設置 */
                padding: 10px;            /* 氣泡內邊距 */
                font-size: 14px;          /* 字體大小 */
                color: #333333;           /* 文字顏色 */
            }
            """
        )
        label.setMinimumWidth(100)
        label.setMaximumWidth(250)
        label.setWordWrap(True)

        # 將氣泡放在左邊或右邊
        if self.is_left:
            layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignLeft)
            layout.addStretch()
        else:
            layout.addStretch()
            layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)


class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat Interface")
        self.setGeometry(200, 200, 400, 600)

        # 主視圖
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 聊天區域
        self.chat_area = QScrollArea()
        self.chat_area.setWidgetResizable(True)
        self.chat_area.setStyleSheet("QScrollArea { border: none; }")

        # 聊天內容容器
        self.chat_content = QWidget()
        self.chat_content.setStyleSheet("background-color: #f7f7f7;")
        self.chat_layout = QVBoxLayout()
        self.chat_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.chat_layout.setSpacing(10)
        self.chat_content.setLayout(self.chat_layout)
        self.chat_area.setWidget(self.chat_content)

        # 按鈕區域
        self.button_layout = QHBoxLayout()
        self.send_left_button = QPushButton("Send Left")
        self.send_right_button = QPushButton("Send Right")
        self.button_layout.addWidget(self.send_left_button)
        self.button_layout.addWidget(self.send_right_button)

        # 主佈局
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.addWidget(self.chat_area)
        main_layout.addLayout(self.button_layout)

        # 信號與槽
        self.send_left_button.clicked.connect(self.add_left_bubble)
        self.send_right_button.clicked.connect(self.add_right_bubble)

    def add_left_bubble(self):
        bubble = ChatBubble("Hello from left!", is_left=True)
        self.chat_layout.addWidget(bubble)

        # 滾動到底部
        self.chat_area.verticalScrollBar().setValue(self.chat_area.verticalScrollBar().maximum())

    def add_right_bubble(self):
        bubble = ChatBubble("Hello from right!", is_left=False)
        self.chat_layout.addWidget(bubble)

        # 滾動到底部
        self.chat_area.verticalScrollBar().setValue(self.chat_area.verticalScrollBar().maximum())
