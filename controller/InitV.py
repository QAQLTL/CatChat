from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from qframelesswindow import StandardTitleBar

from view import QInitView
from model import *
from common import *

datacontroller = DataController()
sslcontroller = SslClass()
settings = Config("Personal")
ip = IPclass()

class InitV(QInitView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitleBar(StandardTitleBar(self))
        self.stackedwidget = StackedWidget()
        self.welcomview = Welcome()
        self.ifsview = InforSetting()
        self.sslcryptoview = SslCrypto()

    def ui_init(self):
        self.titleBar.maxBtn.deleteLater()
        self.titleBar._isDoubleClickEnabled = False

        self.stackedwidget.addWidget(self.welcomview)
        self.Vlayout.addWidget(self.stackedwidget)

        self.ifsview.donebut.clicked.connect(self.add_widget)
        self.stackedwidget.currentChanged.connect(self.anime_start)

        self.welcomview.check_config()

    def anime_start(self, index):
        if self.stackedwidget.get_page_name(index) == "Infor_page":
            self.ifsview.nameedit.start_animation()
            self.stackedwidget.removeWidget(self.sslcryptoview)
        else:
            self.ifsview.nameedit.end_animation()

    def add_widget(self):
        if self.ifsview.nameedit.text() and self.ifsview.circleimage.image():
            image_path = datacontroller.file_copy_path(self.ifsview.circleimage.imagepath, "images",
                                                       "personal_avatar", ".png")
            settings.save_avatar_path(image_path)
            settings.save_username(self.ifsview.nameedit.text())
            settings.save_useripv4(ip.curripv4)
            self.stackedwidget.addWidget(self.sslcryptoview)
            self.stackedwidget.animateToPage(2, "left")

class Welcome(QWidget):
    loadedSignal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.datetime = QDateTime.currentDateTime()
        self.WelcomeLabel = QLabel(self)
        self.vlayout = QVBoxLayout(self)
        self.ui_init()

    def ui_init(self):
        self.setObjectName("welcome_page")
        font = QFont()
        font.setPointSize(40)
        self.WelcomeLabel.setFont(font)
        self.WelcomeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.WelcomeLabel.setText("𝓦𝓮𝓬𝓵𝓸𝓶𝓮")

        self.vlayout.addWidget(self.WelcomeLabel, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.vlayout)

    def check_config(self):
        settings.save_last_time(self.datetime.toString(Qt.DateFormat.ISODate))
        val = settings.load_avatar_path() or settings.load_username() or settings.load_ssl_crypto()
        self.loadedSignal.emit(bool(val))

class InforSetting(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vmlayout = QVBoxLayout(self)
        self.vlayout = QVBoxLayout()
        self.bottomlayout = QHBoxLayout()
        self.circleimage = QAvatarWidget(self)
        self.nameedit = QLineEditBar(self)
        self.donebut = QBorderButton(self, sizew=20, sizeh=20)

        self.ui_init()

    def ui_init(self):
        self.setObjectName("Infor_page")
        self.circleimage.setFixedSize(200, 200)

        self.circleimage.clicked.connect(self.imageevent)

        self.nameedit.setFixedWidth(0)
        self.nameedit.setFixedHeight(30)
        self.nameedit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nameedit.setStyleSheet("""
        QLineEdit {
           font-family: Arial Black;
           font-size: 22px;
           background-color: transparent;
           border-radius: 0px;
           padding: 2px;
           border-bottom: 2px solid #A7A7A7;
           color: #4E4E4E;
        }
        """)

        self.donebut.seticon("D:/python/CatChat/res/left-arrow.png")

        self.vlayout.setSpacing(5)
        self.vlayout.addWidget(self.circleimage, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.vlayout.addWidget(self.nameedit, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        self.vlayout.setContentsMargins(0, 60, 0, 60)

        self.vmlayout.addLayout(self.vlayout)
        self.bottomlayout.addWidget(self.donebut, 0, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)

        self.vmlayout.addLayout(self.bottomlayout)

    def imageevent(self):
        dialog = QFileDialog()
        dialog.setNameFilter("All images (*.png *.jpg)")
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        dialogss = dialog.exec()
        if dialogss:
            filePath = dialog.selectedFiles()
            if filePath:
                self.circleimage.setimage(filePath[0])
            else:
                return
        else:
            return

class ComputerInfor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hlayout = QHBoxLayout(self)
        self.ipv4group = QGroupBox("IPv4")
        self.ipv6group = QGroupBox("IPv6")

        self.ipv4Lable = QLineLabel(self, ip.curripv4)
        self.ipv4layout = QHBoxLayout()
        self.ipv6Lable = QLineLabel(self, ip.curripv6)
        self.ipv6layout = QHBoxLayout()

        self.ui_init()

    def ui_init(self):
        self.ipv4layout.addWidget(self.ipv4Lable)
        self.ipv6layout.addWidget(self.ipv6Lable)

        self.ipv4Lable.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ipv4group.setLayout(self.ipv4layout)
        self.ipv6Lable.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ipv6group.setLayout(self.ipv6layout)

        self.hlayout.setContentsMargins(0, 0, 0, 0)
        self.hlayout.addWidget(self.ipv4group, alignment=Qt.AlignmentFlag.AlignCenter)
        self.hlayout.addWidget(self.ipv6group, alignment=Qt.AlignmentFlag.AlignCenter)

        self.style()

    def style(self):
        self.ipv4Lable.setFixedHeight(20)
        self.ipv6Lable.setFixedHeight(20)
        self.ipv4Lable.setStyleSheet("""
        QLabel {
           font-family: Arial Black;
           font-size: 20px;
           background-color: transparent;
           border-radius: 0px;
           padding: 0px;
           border-bottom: 2px solid #A7A7A7;
           color: #4E4E4E;
        }
        """)
        self.ipv6Lable.setStyleSheet("""
        QLabel {
           font-family: Arial Black;
           font-size: 20px;
           background-color: transparent;
           border-radius: 0px;
           padding: 0px;
           border-bottom: 2px solid #A7A7A7;
           color: #4E4E4E;
        }
        """)
        self.setStyleSheet("""
        QGroupBox {
            font: bold 10px;
            color: #52616B;
            border: 1px solid #A7A7A7;
            border-radius: 5px;
            margin-top: 5px;
        }
        QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 5px;
        }
        """)

class SslCrypto(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)
        self.box_layout = QHBoxLayout()
        self.input_boxes = []
        self.confirm_button = QBorderButton(self, sizew=20, sizeh=20)

        self.key = None
        self.checked = None

        self.ui_init()
        self.update_input_box_styles()

    def ui_init(self):
        self.setObjectName("SSl_page")
        for i in range(4):
            input_box = PasswordInputBox(i, self)
            input_box.setMaxLength(1)
            input_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
            input_box.setEchoMode(QLineEdit.EchoMode.Normal)
            input_box.setPlaceholderText("0")
            # input_box.setInputMask("D")
            input_box.textChanged.connect(lambda text, idx=i: self.on_text_changed(text, idx))
            self.box_layout.addWidget(input_box, 0, alignment=Qt.AlignmentFlag.AlignCenter)
            self.input_boxes.append(input_box)

        self.confirm_button.seticon("D:/python/CatChat/res/left-arrow.png")
        self.confirm_button.clicked.connect(self.check_password)


        self.main_layout.addLayout(self.box_layout)
        self.main_layout.addWidget(self.confirm_button, 0, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
        self.main_layout.setContentsMargins(5, 140, 5, 5)

    def on_text_changed(self, text, idx):
        if text:
            if idx < 3:
                self.input_boxes[idx + 1].setFocus()
            else:
                self.confirm_button.setFocus()

    def check_password(self):
        password = ''.join(box.text() for box in self.input_boxes)
        if settings.load_ssl_crypto():
            key = KeyDecryptor()
            if len(password) == 4:
                if key.try_decrypt(password):
                    self.checked = True
                else:
                    self.checked = False
            else:
                self.checked = False
        else:
            if len(password) == 4:
                sslcontroller.create_key(password)
                settings.save_ssl_crypto(True)
            elif len(password) == 0:
                sslcontroller.create_key()
                settings.save_ssl_crypto(False)

        self.update_input_box_styles()

    def update_input_box_styles(self):
        color = "#A7A7A7"  # 默認灰色
        if self.checked is True:
            color = "#90EE90"  # 淺綠色 (成功)
        elif self.checked is False:
            color = "#F08080"  # 淺紅色 (失敗)

        for input_box in self.input_boxes:
            input_box.setStyleSheet(f"""
                font-size: 30px;
                color: #A7A7A7;
                background-color: transparent;
                border: 2px solid {color};
                border-radius: 5px;
                padding: 15px 5px 15px 5px;
                max-height: 70px;
                max-width: 50px;
            """)

class PasswordInputBox(QLineEdit):
    def __init__(self, index, parent=None):
        super().__init__(parent)
        self.index = index
        self.parent_widget = parent

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Backspace and not self.text():
            if self.index > 0:
                prev_box = self.parent_widget.input_boxes[self.index - 1]
                prev_box.setFocus()
                prev_box.clear()
        else:
            super().keyPressEvent(event)

class LoadingAnimation(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(50, 50)

        self.angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(30)

    def paintEvent(self, event):
        """繪製加載動畫"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        rect = self.rect()
        size = min(rect.width(), rect.height()) // 4


        pen = QPen(Qt.GlobalColor.gray, 5)
        painter.setPen(pen)


        center_x = rect.width() // 2
        center_y = rect.height() // 2


        painter.translate(center_x, center_y)
        painter.rotate(self.angle)
        painter.drawArc(-size, -size, size * 2, size * 2, 0, 120 * 16)

    def update_animation(self):
        """更新動畫角度並刷新界面"""
        self.angle = (self.angle + 5) % 360
        self.update()