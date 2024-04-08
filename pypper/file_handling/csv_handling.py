import csv
import os
from typing import Dict, List


class CSVHandler:
    """
    A class to handle CSV files
    """

    def __init__(self):
        pass

    def create_csv_if_not_exists(self, csv_path: str, field_names: List[str]) -> None:
        """
        Create a csv file with the given field names if it does not exist.
        :param csv_path: Path to the csv file.
        :param field_names: List of field names.
        :return: None
        """
        if not os.path.exists(csv_path):
            with open(csv_path, "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()

    def append_to_csv(self, file_path: str, data: Dict) -> None:
        """
        Append data to a csv file.
        :param file_path: Path to the csv file.
        :param data: Data to append.
        :return: None
        """
        with open(file_path, "a", newline="") as csvfile:
            fieldnames = data.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(data)
