from PyQt6 import QtWidgets, QtCore


class QHInformat(QtWidgets.QWidget):
    def __init__(self, parent=None):  # 修正這裡的錯誤
        super().__init__(parent=parent)
        self.resize(250, 250)
        sizepolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizepolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizepolicy)
        self.setMinimumSize(QtCore.QSize(250, 250))
        self.setMaximumSize(QtCore.QSize(250, 250))

        # 設置垂直佈局
        self.vlayout = QtWidgets.QVBoxLayout(self)

        # 創建並添加 informat_widget
        self.informat_widget = QtWidgets.QWidget(parent=self)
        self.vlayout.addWidget(self.informat_widget)

        # informat_widget 的佈局設置
        self.informat_vlayout = QtWidgets.QVBoxLayout(self.informat_widget)
        self.informat_widget.setStyleSheet(
            "QWidget {\n"
            "background: rgb(206, 255, 255);\n"
            "border-radius: 20px;\n"
            "}"
        )