import os
import shutil
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