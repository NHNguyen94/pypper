from datetime import datetime

import numpy as np
import pandas as pd


class DateTimeProcessor():
    def __init__(self):
        pass

    @staticmethod
    def get_current_utc_timestamp() -> str:
        current_timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        return current_timestamp

    @staticmethod
    def get_current_local_timestamp() -> str:
        current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return current_timestamp

    def cast_str_to_datetime(self, date_str: str, datetime_format: str) -> datetime:
        return datetime.strptime(date_str, datetime_format)

    def _vectorized_cast_str_to_datetime(self,
                                         date_str: np.array,
                                         datetime_format: str) -> np.array:
        return np.vectorize(self.cast_str_to_datetime)(date_str, datetime_format)

    def cast_string_to_datetime_in_df(self,
                                      df: pd.DataFrame,
                                      column: str, datetime_format: str
                                      ) -> pd.DataFrame:
        df[column] = self._vectorized_cast_str_to_datetime(df[column], datetime_format)
        return df
