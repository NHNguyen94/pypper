from unittest import TestCase

import pandas as pd

from pypper.data_processing.datetime.datetime_processing import DateTimeProcessor


class TestDateTimeProcessor(TestCase):
    def test_cast_str_to_datetime(self):
        print("Test function cast_str_to_datetime")
        datetime_processor = DateTimeProcessor()
        date_str = "2021-01-01 12:00:00"
        datetime_format = "%Y-%m-%d %H:%M:%S"
        datetime_obj = datetime_processor.cast_str_to_datetime(
            date_str=date_str, datetime_format=datetime_format
        )
        print(datetime_obj)
        self.assertEqual(datetime_obj.year, 2021)
        self.assertEqual(datetime_obj.month, 1)
        self.assertEqual(datetime_obj.day, 1)
        self.assertEqual(datetime_obj.hour, 12)
        self.assertEqual(datetime_obj.minute, 0)
        self.assertEqual(datetime_obj.second, 0)

    def test_cast_str_to_datetime_in_df(self):
        print("Test function cast_str_to_datetime_in_df")
        datetime_processor = DateTimeProcessor()
        df = pd.DataFrame({"date_str": ["2021-01-01 12:00:00", "2021-01-02 12:00:00"]})
        datetime_format = "%Y-%m-%d %H:%M:%S"
        df = datetime_processor.cast_string_to_datetime_in_df(
            df=df,
            datetime_str_col_name="date_str",
            casted_col_name="date_time",
            datetime_format=datetime_format,
        )
        print(df)
        print(df.info())
        self.assertEqual(df["date_time"].dtypes, "datetime64[ns]")
        self.assertEqual(df["date_time"][0].year, 2021)
        self.assertEqual(df["date_time"][0].month, 1)
        self.assertEqual(df["date_time"][0].day, 1)
        self.assertEqual(df["date_time"][0].hour, 12)
        self.assertEqual(df["date_time"][0].minute, 0)
        self.assertEqual(df["date_time"][0].second, 0)
        self.assertEqual(df["date_time"][1].year, 2021)
        self.assertEqual(df["date_time"][1].month, 1)
        self.assertEqual(df["date_time"][1].day, 2)
        self.assertEqual(df["date_time"][1].hour, 12)
        self.assertEqual(df["date_time"][1].minute, 0)
        self.assertEqual(df["date_time"][1].second, 0)
