import os
import shutil
import json
from pathlib import Path

class DataController:
    def __init__(self):
        self.base_path = Path(f"{os.getcwd()}/data").as_posix()
        self.base_path_create(self.base_path)

    def base_path_create(self, path):
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)
            return False
        else:
            return True

    def file_copy_path(self, filepath:str, foldername:str, filename:str, file_extension:str):
        filename_path = self.base_path + f"/{foldername}/"

        if self.base_path_create(filename_path):
            shutil.copyfile(filepath, filename_path + filename + file_extension)
            return filename_path + filename + file_extension
        else:
            shutil.copyfile(filepath, filename_path + filename + file_extension)
            return filename_path + filename + file_extension


class FriendManager:
    def __init__(self, file_path):
        """
        初始化好友管理器
        :param file_path: 存储好友数据的 JSON 文件路径
        """
        self.file_path = file_path
        self.friends = []
        self.load_from_json()  # 自动加载现有数据

    def add_friend(self, name, avatar_path, ipv4=None, ipv6=None, publickey_path=None, status="等待加好友"):
        """
        添加好友到内存数据，如果好友已存在，则不添加
        :param name: 好友名称
        :param avatar_path: 头像路径
        :param ipv4: IPv4 地址（可选）
        :param ipv6: IPv6 地址（可选）
        :param publickey_path: 公钥路径（可选）
        :param status: 好友状态（默认是“等待加好友”）
        """
        # 检查是否已经存在相同的好友（根据 name 或 publickey_path 判断）
        for friend in self.friends:
            if friend["name"] == name or (publickey_path and friend.get("publickey_path") == publickey_path):
                print(f"好友 {name} 已存在，无法重复添加")
                return

        # 添加新的好友
        friend = {
            "name": name,
            "avatar_path": avatar_path,
            "ipv4": ipv4,
            "ipv6": ipv6,
            "publickey_path": publickey_path,
            "status": status,
        }
        self.friends.append(friend)
        print(f"好友 {name} 已成功添加")

    def update_friend_status(self, name, new_status):
        """
        更新指定好友的状态
        :param name: 好友名称
        :param new_status: 新的状态
        """
        for friend in self.friends:
            if friend["name"] == name:
                friend["status"] = new_status
                print(f"已更新好友 {name} 的状态为 {new_status}")
                return
        print(f"未找到名为 {name} 的好友")

    def save_to_json(self):
        """
        将好友数据保存到 JSON 文件（增量更新）
        """
        # 如果文件存在，加载现有数据，合并新数据
        existing_data = []
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as json_file:
                    existing_data = json.load(json_file)
            except json.JSONDecodeError:
                print("现有文件内容无效，将覆盖保存新文件。")

        # 合并数据（避免重复）
        existing_names = {friend["name"] for friend in existing_data}
        for friend in self.friends:
            if friend["name"] not in existing_names:
                existing_data.append(friend)

        # 保存数据
        try:
            with open(self.file_path, 'w', encoding='utf-8') as json_file:
                json.dump(existing_data, json_file, indent=4, ensure_ascii=False)
            print(f"好友数据已保存到 {self.file_path}")
        except Exception as e:
            print(f"保存好友数据时出错: {e}")

    def load_from_json(self):
        """
        从 JSON 文件加载好友数据
        """
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as json_file:
                    self.friends = json.load(json_file)
                print(f"好友数据已从 {self.file_path} 加载")
            except json.JSONDecodeError:
                print(f"文件 {self.file_path} 格式错误，无法加载好友数据")
        else:
            print(f"文件 {self.file_path} 不存在，无法加载好友数据")

    def list_friends(self):
        """
        列出所有好友数据
        """
        if not self.friends:
            print("好友列表为空")
            return

        for index, friend in enumerate(self.friends, start=1):
            print(f"好友 {index}:")
            for key, value in friend.items():
                print(f"  {key}: {value}")
            print()