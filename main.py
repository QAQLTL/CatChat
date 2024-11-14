import sys

from PyQt6.QtWidgets import QApplication

from controller import MainV

class Window(MainV):
    def __init__(self):
        super().__init__()
        qr = self.frameGeometry()  # 得到一个指定主窗口几何形状的矩形
        cp = self.screen().availableGeometry().center()  # 计算出显示器的分辨率，通过分辨率得出中心点
        qr.moveCenter(cp)  # 设置为屏幕的中心，矩形大小不变
        self.move(qr.topLeft())  # 将应用程序的左上角移动到矩形的左上角，使屏幕在窗口正中


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()

