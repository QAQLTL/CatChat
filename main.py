from PySide6.QtUiTool import QUiLoader
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])
    
    loader = QUiLoader()
    hb_window = loader.load("uichat.ui")
    hb_window.show()

    app.exec()