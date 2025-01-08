import os
import shutil
from pathlib import Path
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

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

Base = declarative_base()
datac = DataController()

class User(Base):
    __tablename__ = "users"

    avatar_path = Column(String, nullable=False)
    name = Column(String, nullable=False, primary_key=True)  # 使用 `name` 作為唯一主鍵
    ipv4 = Column(String, nullable=True)
    ipv6 = Column(String, nullable=True)
    public_key = Column(String, nullable=True)

class UserDataManager:
    def __init__(self, db_name="usesrsdata"):
        datac.base_path_create(datac.base_path+"/sql")
        self.engine = create_engine(f'sqlite:///data/sql/{db_name}.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_user(self, avatar_path, name, ipv4=None, ipv6=None, public_key=None):
        session = self.Session()
        try:
            user = User(
                avatar_path=avatar_path,
                name=name,
                ipv4=ipv4,
                ipv6=ipv6,
                public_key=public_key,
            )
            session.add(user)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_all_users(self):
        session = self.Session()
        try:
            users = session.query(User).all()
            if not users:
                # 如果查詢結果為空，返回空列表或提示消息
                print("No users found in the database.")
                return []
            return [
                {
                    "avatar_path": user.avatar_path,
                    "name": user.name,
                    "ipv4": user.ipv4,
                    "ipv6": user.ipv6,
                    "public_key": user.public_key,
                }
                for user in users
            ]
        finally:
            session.close()

    def update_user(self, name, avatar_path=None, ipv4=None, ipv6=None, public_key=None):
        session = self.Session()
        try:
            user = session.query(User).filter_by(name=name).first()
            if not user:
                raise ValueError(f"No user found with name: {name}")
            if avatar_path:
                user.avatar_path = avatar_path
            if ipv4:
                user.ipv4 = ipv4
            if ipv6:
                user.ipv6 = ipv6
            if public_key:
                user.public_key = public_key
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete_user(self, name):
        session = self.Session()
        try:
            user = session.query(User).filter_by(name=name).first()
            if user:
                session.delete(user)
                session.commit()
            else:
                raise ValueError(f"No user found with name: {name}")
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()