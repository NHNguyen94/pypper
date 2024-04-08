from datetime import datetime

import numpy as np
import pandas as pd


class DateTimeProcessor:
    """
    A class to process datetime
    """

    def __init__(self):
        pass

    @staticmethod
    def get_current_utc_timestamp() -> str:
        """
        Get the current UTC timestamp
        :return: str: The current UTC timestamp
        """
        current_timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        return current_timestamp

    @staticmethod
    def get_current_local_timestamp() -> str:
        """
        Get the current local timestamp
        :return: str: The current local timestamp
        """
        current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return current_timestamp

    def cast_str_to_datetime(self, date_str: str, datetime_format: str) -> datetime:
        """
        Cast a string to a datetime object
        :param date_str: datetime string to cast
        :param datetime_format: datetime format
        :return: datetime object
        """
        return datetime.strptime(date_str, datetime_format)

    def _vectorized_cast_str_to_datetime(
        self, date_str: np.array, datetime_format: str
    ) -> np.array:
        """
        Vectorized version of cast_str_to_datetime
        :param date_str: datetime string to cast
        :param datetime_format: datetime format
        :return: datetime object
        """
        func = np.vectorize(self.cast_str_to_datetime)
        return func(date_str, datetime_format)

    def cast_string_to_datetime_in_df(
        self,
        df: pd.DataFrame,
        datetime_str_col_name: str,
        casted_col_name: str,
        datetime_format: str,
    ) -> pd.DataFrame:
        """
        Cast a string column to a datetime column in a dataframe
        :param df: Pandas DataFrame
        :param datetime_str_col_name: column name of the datetime string
        :param casted_col_name: column name of the casted datetime
        :param datetime_format: datetime format
        :return: Pandas DataFrame
        """
        df[casted_col_name] = self._vectorized_cast_str_to_datetime(
            df[datetime_str_col_name], datetime_format
        )
        return df
