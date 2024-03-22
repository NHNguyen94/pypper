import os
import shutil


class FileSystemHandler():
    """
    A class to handle file system operations
    """
    def __init__(self):
        pass

    def create_folder_path(self, folder_path: str) -> None:
        """
        Create a folder path if it does not exist.
        :param folder_path: Path to the folder.
        :return: None
        """
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        else:
            pass

    def delete_folder(self, folder_path: str) -> None:
        """
        Delete a folder.
        :param folder_path: Path to the folder.
        :return: None
        """
        if os.path.exists(folder_path):
            os.rmdir(folder_path)
        else:
            pass

    def delete_not_empty_folder(self, folder_path: str) -> None:
        """
        Delete a folder even if it is not empty.
        :param folder_path: Path to the folder.
        :return: None
        """
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        else:
            pass
