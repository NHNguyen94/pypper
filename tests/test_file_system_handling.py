from unittest import TestCase
from pypper.file_handling.file_system_handling import FileSystemHandler


class TestFileSystemHandler(TestCase):
    def test_create_folder_path(self):
        print("Test function create_folder_path")
        folder_path = "tests/output_for_tests/test_folder"
        file_system_handler = FileSystemHandler()
        # Create a folder
        file_system_handler.create_folder_path(folder_path=folder_path)
        # Check if the folder is created
        self.assertTrue(
            file_system_handler.check_folder_existence(folder_path=folder_path)
        )

    def test_delete_folder_path(self):
        print("Test function delete_folder_path")
        folder_path = "tests/output_for_tests/test_folder"
        file_system_handler = FileSystemHandler()
        # Delete the folder
        file_system_handler.delete_not_empty_folder(folder_path=folder_path)
        # Check if the folder is deleted
        self.assertFalse(
            file_system_handler.check_folder_existence(folder_path=folder_path)
        )
