import sys
from PyQt6 import QtWidgets
from uichat import Ui_MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    maw = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(maw)
    maw.show()
    sys.exit(app.exec())