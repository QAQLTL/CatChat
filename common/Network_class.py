import socket
import requests
from typing import List
from Cryptodome.PublicKey import RSA


class IPclass:
    def __init__(self):
        self.curripv4:str = ""
        self.curripv6:str = ""
        self.serveriplist:List[str]
        self.hostname = socket.gethostname()

        self.getcurrip()

    def check_internet(self, url="https://www.google.com", timeout=1):
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                print(f"成功訪問 {url}")
                return True
        except requests.ConnectionError:
            print(f"無法連接到 {url}")
        except requests.Timeout:
            print(f"連接到 {url} 超時")
        return False

    def getcurrip(self):
        try:
            for info in socket.getaddrinfo(self.hostname, None):
                family, _, _, _, sockaddr = info
                ip = sockaddr[0]
                if family == socket.AF_INET:
                    self.curripv4 = ip
                elif family == socket.AF_INET6:
                    self.curripv6 = ip
        except Exception as e:
            print(f"Error getting IP addresses: {e}")


class Sslclass:
    def __init__(self):
        self.key = RSA.generate(2048)
        self.private:str = ""
        self.public:str = ""

        self.create_key()

    def create_key(self):
        self.private = self.key.export_key()
        self.public = self.key.publickey().export_key()

        with open("privateKey.pem", "wb") as f:
            f.write(self.private)

        with open("publicKey.pem", "wb") as f:
            f.write(self.public)

