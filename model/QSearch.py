from PyQt6.QtWidgets import (
    QLineEdit,
    QHBoxLayout,
    QWidget,
)

class SearchApp(QWidget):
    def __init__(self):
        super().__init__()

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("輸入搜尋內容...")
        self.search_bar.setStyleSheet(
            """
            QLineEdit {
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
            """
        )

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_bar)
        self.setLayout(search_layout)