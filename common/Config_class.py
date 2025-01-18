from PyQt6.QtCore import QSettings

class Config(QSettings):
    def __init__(self, childfile=None):
        super().__init__("CatChat", childfile)

    def load_avatar_path(self) -> str:
        return self.value("avatarPath")

    def load_username(self) -> str:
        return self.value("username")

    def load_useripv4(self) -> str:
        return self.value("useripv4")

    def load_last_time(self) -> str:
        return self.value("lastTime")

    def load_ssl_crypto(self) -> str:
        return self.value("SSlCrypto")

    def save_avatar_path(self, path:str):
        return self.setValue("avatarPath", path)

    def save_username(self, username: str):
        return self.setValue("username", username)

    def save_useripv4(self, useripv4:str):
        return self.setValue("useripv4", useripv4)

    def save_last_time(self, lasttime:str):
        return self.setValue("lastTime", lasttime)

    def save_ssl_crypto(self, sslcrypto):
        return self.setValue("SSlCrypto", sslcrypto)
