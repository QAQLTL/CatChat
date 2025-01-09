import os
import socket
import requests
from typing import List
from Cryptodome.PublicKey import RSA
from PyQt6.QtCore import *

import traceback
import threading
import time
import json

from .DataController_class import DataController

base_uuid = "123e4567-e89b-12d3-a456-426614174000"

datacontroller = DataController()

class IPclass:
    def __init__(self):
        self.curripv4: str = ""
        self.curripv6: str = ""
        self.serveriplist: List[str] = []
        self.hostname = socket.gethostname()

        self.getcurrip()

    def check_internet(self, url="https://www.google.com", timeout=1):
        """檢查是否能連接到指定網址以驗證網路連線。"""
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
        """取得本機的 IPv4 和 IPv6 位址。"""
        try:
            ipv4_set = set()
            ipv6_set = set()
            for info in socket.getaddrinfo(self.hostname, None):
                family, _, _, _, sockaddr = info
                ip = sockaddr[0]
                if family == socket.AF_INET:
                    ipv4_set.add(ip)
                elif family == socket.AF_INET6:
                    ipv6_set.add(ip)

            # 確保選取第一個有效地址
            self.curripv4 = next(iter(ipv4_set), "")
            self.curripv6 = next(iter(ipv6_set), "")

            # 儲存所有找到的 IP 地址
            self.serveriplist = list(ipv4_set.union(ipv6_set))
        except Exception as e:
            print(f"Error getting IP addresses: {e}")

    def get_ipv4(self) -> str:
        return self.curripv4

    def get_ipv6(self) -> str:
        return self.curripv6

class SslClass:
    def __init__(self):
        self.private: str = ""
        self.public: str = ""

        self.path = os.path.join(datacontroller.base_path, "sslkey")

    def save_key(self, private_key: bytes, public_key: bytes):
        """
        保存私鑰和公鑰到文件。
        :param private_key: 私鑰的字節數據。
        :param public_key: 公鑰的字節數據。
        """
        private_path = os.path.join(self.path, "private.pem")
        public_path = os.path.join(self.path, "public.pem")
        try:
            with open(private_path, 'wb') as priv_file:
                priv_file.write(private_key)
            with open(public_path, 'wb') as pub_file:
                pub_file.write(public_key)
            print(f"[INFO] 密鑰已保存到 {private_path} 和 {public_path}")
        except Exception as e:
            print(f"[ERROR] 保存密鑰時出現錯誤: {e}")
            traceback.print_exc()

    def create_key(self, cryptocode: str = None):
        """
        生成 RSA 密鑰對，根據是否提供密碼來加密私鑰。
        :param cryptocode: 用於加密私鑰的密碼（如果提供）。
        :return: (私鑰, 公鑰) 的字節數據。
        """
        datacontroller.base_path_create(self.path)  # 確保目標目錄存在
        try:
            # 生成 2048 位的 RSA 密鑰
            key = RSA.generate(2048)

            # 導出私鑰
            if cryptocode:
                private_key = key.export_key(passphrase=cryptocode, pkcs=8, protection="scryptAndAES128-CBC")
            else:
                private_key = key.export_key()

            # 導出公鑰
            public_key = key.publickey().export_key()

            # 保存密鑰
            self.save_key(private_key, public_key)

            print("[INFO] 密鑰生成成功！")
            return private_key, public_key
        except Exception as e:
            print(f"[ERROR] 生成密鑰時出現錯誤: {e}")
            traceback.print_exc()
            return None, None

class KeyDecryptor:
    def __init__(self):
        """
        初始化 KeyDecryptor 類。
        :param encrypted_key_path: 加密私鑰文件的路徑。
        """
        self.key = None
        self.path = os.path.join(datacontroller.base_path, "sslkey")
        self.load_encrypted_key()

    def load_encrypted_key(self):
        """
        加載加密的私鑰。
        :return: 私鑰的字節數據。
        """
        try:
            with open(os.path.join(self.path, "private.pem"), 'rb') as file:
                encrypted_key = file.read()
            return encrypted_key
        except FileNotFoundError:
            print(f"[ERROR] 文件未找到: private.pem")
        except Exception as e:
            print(f"[ERROR] 加載加密私鑰時發生錯誤: {e}")
            traceback.print_exc()
        return None

    def try_decrypt(self, password: str) -> bool:
        """
        嘗試使用提供的密碼解密加密私鑰。
        :param password: 用於解密私鑰的密碼。
        :return: 解密是否成功（True or False）。
        """
        encrypted_key = self.load_encrypted_key()
        if not encrypted_key:
            return False

        try:
            self.key = RSA.import_key(encrypted_key, passphrase=password)
            print("[INFO] 解密成功！")
            return True
        except ValueError:
            print("[WARNING] 解密失敗，密碼可能不正確。")
        except Exception as e:
            print(f"[ERROR] 解密過程中發生錯誤: {e}")
            traceback.print_exc()

        return False

class NetCatCHAT(QObject):
    devices_updated = pyqtSignal(list)

    BROADCAST_PORT = 50000
    BROADCAST_ADDR = '<broadcast>'
    BUFFER_SIZE = 1024
    TIMEOUT_THRESHOLD = 5

    def __init__(self):
        super().__init__()
        self.identifier = {
            "program": "CatCHAT",
            "version": "1.0",
            "uuid": base_uuid,
            "username": None
        }
        self.own_ip = 'self.get_own_ip()'
        self.stop_listener = threading.Event()
        self.stop_broadcast = threading.Event()
        self.sender_thread = None
        self.listener_thread = None
        self.clean_up_thread = None
        self.found_devices = []

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
            last_log_time = time.time()  # 用於限制日誌的頻率
            while not self.stop_broadcast.is_set():
                sender.sendto(message, (self.BROADCAST_ADDR, self.BROADCAST_PORT))
                current_time = time.time()
                if current_time - last_log_time >= 10:  # 每隔5秒記錄一次日誌
                    print("[INFO] 廣播訊息已發送")
                    last_log_time = current_time
                time.sleep(1)

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

            last_device_log_time = time.time()  # 控制日誌輸出的頻率
            while not self.stop_listener.is_set():
                try:
                    listener.settimeout(1)
                    data, addr = listener.recvfrom(self.BUFFER_SIZE)
                    try:
                        message = json.loads(data.decode('utf-8'))
                        if message.get("program") == self.identifier["program"] and addr[0] != self.own_ip:
                            existing_device = next((d for d in self.found_devices if d['ip'] == addr[0]), None)
                            if existing_device:
                                existing_device["last_seen"] = time.time()
                            else:
                                self.found_devices.append({
                                    "ip": addr[0],
                                    "username": message.get("username", "Unknown"),
                                    "last_seen": time.time()
                                })
                            self.devices_updated.emit(self.found_devices)
                            current_time = time.time()
                            if current_time - last_device_log_time >= 15:  # 每隔5秒記錄一次日誌
                                print(f"[INFO] 收到來自相同程式的電腦: {addr[0]} (用戶名: {message.get('username')})")
                                last_device_log_time = current_time
                    except (UnicodeDecodeError, json.JSONDecodeError):
                        print(f"[WARNING] 收到無法解碼的訊息，來自: {addr}")
                except socket.timeout:
                    continue

    def clean_up_devices(self):
        """移除超時未回應的設備。"""
        while not self.stop_listener.is_set():
            time.sleep(1)
            current_time = time.time()
            removed_devices = [
                d for d in self.found_devices if current_time - d["last_seen"] > self.TIMEOUT_THRESHOLD
            ]

            for device in removed_devices:
                self.found_devices.remove(device)
                print(f"[INFO] 移除超時未回應的設備: {device['ip']}")

            if removed_devices:
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

    def update_name(self, name):
        self.identifier["username"] = name

class UDPServer:
    def __init__(self, port: int = 12345):
        self.ip_class = IPclass()
        self.port = port
        self.sockets = []
        self.running = False
        self.callback = None

    def set_callback(self, callback):
        """设置收到消息后的回调函数"""
        self.callback = callback

    def start_server(self):
        self.running = True
        threading.Thread(target=self.run_server, daemon=True).start()

    def run_server(self):
        try:
            # IPv4 Socket
            ipv4 = self.ip_class.get_ipv4()
            if ipv4:
                ipv4_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                ipv4_socket.bind((ipv4, self.port))
                self.sockets.append(ipv4_socket)
                print(f"[INFO] 伺服器啟動於 [IPv4] {ipv4}:{self.port}")
            # IPv6 Socket
            ipv6 = self.ip_class.get_ipv6()
            if ipv6:
                ipv6_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
                ipv6_socket.bind((ipv6, self.port, 0, 0))
                self.sockets.append(ipv6_socket)
                print(f"[INFO] 伺服器啟動於 [IPv6] {ipv6}:{self.port}")
            if not self.sockets:
                if self.callback:
                    self.callback("[ERROR] 無法取得任何有效的 IP 地址。")
                return

            while self.running:
                for sock in self.sockets:
                    sock.settimeout(1.0)
                    try:
                        data, addr = sock.recvfrom(1024)
                        if self.callback:
                            self.callback(f"[INFO] 收到來自 {addr} 的訊息: {data.decode('utf-8')}")
                    except socket.timeout:
                        continue
        except Exception as e:
            if self.callback:
                self.callback(f"[ERROR] 伺服器錯誤: {e}")
        finally:
            for sock in self.sockets:
                sock.close()

    def stop_server(self):
        self.running = False

class UDPClient:
    def __init__(self, server_ip: str, server_port: int = 12345, use_ipv6: bool = False):
        self.ip_class = IPclass()
        self.server_ip = server_ip
        self.server_port = server_port
        self.use_ipv6 = use_ipv6
        self.socket = socket.socket(
            socket.AF_INET6 if use_ipv6 else socket.AF_INET, socket.SOCK_DGRAM
        )

    def send_message(self, message: str):
        try:
            if self.use_ipv6:
                ipv6 = self.ip_class.get_ipv6()
                if not ipv6:
                    print("[ERROR] 無法取得 IPv6 地址。")
                    return
                self.socket.sendto(
                    message.encode('utf-8'), (self.server_ip, self.server_port, 0, 0)
                )
                print(f"[INFO] 訊息已發送到 [IPv6] {self.server_ip}:{self.server_port}: {message}")
            else:
                ipv4 = self.ip_class.get_ipv4()
                if not ipv4:
                    print("[ERROR] 無法取得 IPv4 地址。")
                    return
                self.socket.sendto(message.encode('utf-8'), (self.server_ip, self.server_port))
                print(f"[INFO] 訊息已發送到 [IPv4] {self.server_ip}:{self.server_port}: {message}")
        except Exception as e:
            print(f"[ERROR] 傳送訊息時發生錯誤: {e}")
        finally:
            self.socket.close()