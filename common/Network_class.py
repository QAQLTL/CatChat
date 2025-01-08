import os
import socket
import requests
from typing import List
from Cryptodome.PublicKey import RSA
from PyQt6.QtCore import *

import threading
import time
import json

from .DataController_class import DataController

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


class SslClass:
    def __init__(self):
        self.private: str = ""
        self.public: str = ""

        self.datacontroller = DataController()
        self.path = os.path.join(self.datacontroller.base_path, "sslkey")

    def save_key(self, private_key, public_key):
        """
        将私钥和公钥保存到指定路径
        """
        try:
            with open(f"{self.path}/privateKey.pem", "wb") as f:
                f.write(private_key)
            with open(f"{self.path}/publicKey.pem", "wb") as f:
                f.write(public_key)
            print("Keys successfully saved.")
        except Exception as e:
            print(f"Error saving keys: {e}")

    def create_key(self, cryptocode: str = None):
        self.datacontroller.base_path_create(self.path)
        key = RSA.generate(2048)

        if cryptocode:
            try:
                # 加密私钥并导出
                private = key.export_key(passphrase=cryptocode, pkcs=8, protection="scryptAndAES128-CBC")
                public = key.publickey().export_key()
                # 保存加密的私钥和公钥
                self.save_key(private, public)
            except Exception as e:
                print(f"Error generating encrypted keys: {e}")
        else:
            try:
                # 未加密的私钥和公钥
                private = key.export_key()
                public = key.publickey().export_key()
                # 保存未加密的私钥和公钥
                self.save_key(private, public)
            except Exception as e:
                print(f"Error generating keys: {e}")


class NetCatCHAT(QObject):
    # 定義信號
    devices_updated = pyqtSignal(list)

    BROADCAST_PORT = 50000
    BROADCAST_ADDR = '<broadcast>'
    BUFFER_SIZE = 1024
    TIMEOUT_THRESHOLD = 5  # 單位: 秒，超過這段時間未收到回應的 IP 會被移除

    def __init__(self, username):
        super().__init__()
        self.identifier = {
            "program": "CatCHAT",
            "version": "1.0",
            "uuid": "123e4567-e89b-12d3-a456-426614174000",
            "username": username  # 新增用戶名
        }
        self.own_ip = 'self.get_own_ip()'
        self.stop_listener = threading.Event()
        self.stop_broadcast = threading.Event()
        self.sender_thread = None
        self.listener_thread = None
        self.clean_up_thread = None
        self.found_devices = []  # 用於存儲設備資訊，每個設備是一個字典

    def get_own_ip(self):
        """取得本機的 IP 位址，用於過濾自身訊息。"""
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            try:
                s.connect(("8.8.8.8", 80))
                return s.getsockname()[0]
            except Exception:
                return "127.0.0.1"

    def send_broadcast(self):
        """發送廣播訊息。"""
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as sender:
            sender.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            message = json.dumps(self.identifier).encode('utf-8')
            while not self.stop_broadcast.is_set():
                sender.sendto(message, (self.BROADCAST_ADDR, self.BROADCAST_PORT))
                print("[INFO] 廣播訊息已發送")
                time.sleep(1)  # 加入延遲以減少網路流量和 CPU 使用率

    def listen_for_responses(self):
        """接收來自其他電腦的訊息。"""
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as listener:
            listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                listener.bind(("", self.BROADCAST_PORT))
                print(f"[INFO] 正在監聽廣播埠 {self.BROADCAST_PORT} ...")
            except OSError as e:
                print(f"[ERROR] 無法綁定到埠 {self.BROADCAST_PORT}: {e}")
                return

            while not self.stop_listener.is_set():
                try:
                    listener.settimeout(1)  # 設置超時以便檢查停止事件
                    data, addr = listener.recvfrom(self.BUFFER_SIZE)
                    try:
                        message = json.loads(data.decode('utf-8'))
                        if message.get("program") == self.identifier["program"] and addr[0] != self.own_ip:
                            # 查找是否已存在該設備
                            existing_device = next((d for d in self.found_devices if d['ip'] == addr[0]), None)
                            if existing_device:
                                # 更新最後回應時間
                                existing_device["last_seen"] = time.time()
                            else:
                                # 新增設備
                                self.found_devices.append({
                                    "ip": addr[0],
                                    "username": message.get("username", "Unknown"),
                                    "last_seen": time.time()
                                })
                            # 發出信號
                            self.devices_updated.emit(self.found_devices)
                            print(f"[INFO] 收到來自相同程式的電腦: {addr[0]} (用戶名: {message.get('username')})")
                    except (UnicodeDecodeError, json.JSONDecodeError):
                        print(f"[WARNING] 收到無法解碼的訊息，來自: {addr}")
                except socket.timeout:
                    continue

    def clean_up_devices(self):
        """移除超時未回應的設備。"""
        while not self.stop_listener.is_set():
            time.sleep(1)  # 每秒檢查一次
            current_time = time.time()
            removed_devices = [
                d for d in self.found_devices if current_time - d["last_seen"] > self.TIMEOUT_THRESHOLD
            ]

            for device in removed_devices:
                self.found_devices.remove(device)
                print(f"[INFO] 移除超時未回應的設備: {device['ip']}")

            if removed_devices:
                # 發出信號
                self.devices_updated.emit(self.found_devices)

    def start_broadcast(self):
        """啟動廣播線程。"""
        if not self.sender_thread or not self.sender_thread.is_alive():
            self.stop_broadcast.clear()
            self.sender_thread = threading.Thread(target=self.send_broadcast)
            self.sender_thread.start()

    def stop_broadcasting(self):
        """停止廣播線程。"""
        self.stop_broadcast.set()
        if self.sender_thread:
            self.sender_thread.join()

    def start_listen(self):
        """啟動監聽線程。"""
        if not self.listener_thread or not self.listener_thread.is_alive():
            self.stop_listener.clear()
            self.listener_thread = threading.Thread(target=self.listen_for_responses)
            self.listener_thread.start()

        if not self.clean_up_thread or not self.clean_up_thread.is_alive():
            self.clean_up_thread = threading.Thread(target=self.clean_up_devices)
            self.clean_up_thread.start()

    def stop_listen(self):
        """停止監聽線程。"""
        self.stop_listener.set()
        if self.listener_thread:
            self.listener_thread.join()
        if self.clean_up_thread:
            self.clean_up_thread.join()
