import sys

from PyQt6.QtWidgets import QApplication

from common import *
from controller import *

settings = Config("Personal")

class Window(InitV):
    def __init__(self, parent=None):
        super().__init__(parent)
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.welcomview.loadedSignal.connect(self.ui_controller)
        self.ui_init()

    def ui_controller(self, val):
        if val:
            if settings.load_ssl_crypto() == "false":
                self.ui_chagne()
            else:
                self.stackedwidget.addWidget(self.sslcryptoview)
                self.sslcryptoview.confirm_button.clicked.connect(self.ui_chagne)
        else:
            self.stackedwidget.addWidget(self.ifsview)
            self.sslcryptoview.confirm_button.clicked.connect(self.ui_chagne)

    def ui_chagne(self):
        try:
            MainUi = MainV()
            screen_geometry = self.screen().availableGeometry()
            screen_x = screen_geometry.x()
            screen_height = screen_geometry.height()

            main_ui_width = MainUi.width()
            main_ui_height = MainUi.height()
            vertical_center = screen_geometry.y() + (screen_height - main_ui_height) // 2

            MainUi.setGeometry(
                screen_x + 15,
                vertical_center,
                main_ui_width,
                main_ui_height
            )
            MainUi.show()
            self.setParent(MainUi)
            self.hide()
            MainUi.update()
        except Exception as e:
            print(f"UI切換錯誤: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()