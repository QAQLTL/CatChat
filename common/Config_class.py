from PyQt6.QtCore import QSettings

class Config(QSettings):
    def __init__(self, childfile=None):
        super().__init__("CatChat", childfile)

    def load_avatar_path(self) -> str:
        """加載用戶的 avatar 圖片路徑，如果不存在則返回默認值"""
        return self.value("avatarPath")

    def load_username(self) -> str:
        """加載用戶名字，如果不存在則返回默認值"""
        return self.value("username")

    def load_useripv4(self) -> str:
        return self.value("useripv4")

    def save_avatar_path(self, path:str):
        """保存用戶的 avatar 圖片路徑"""
        self.setValue("avatarPath", path)

    def save_username(self, username: str):
        """保存用戶名字"""
        self.setValue("username", username)

    def save_useripv4(self, useripv4:str):
        return self.setValue("useripv4", useripv4)