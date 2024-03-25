from unittest import TestCase

import pandas as pd

from pypper.data_processing.tabular.df_processing import DFProcessor


class TestDFProcessor(TestCase):
    def test_drop_outliers(self):
        print("Test function drop_outliers")
        df = pd.DataFrame({"A": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
        threshold = 5
        df_processor = DFProcessor()
        df_no_outliers = df_processor.drop_outliers(df, "A", threshold)
        print(df_no_outliers)
        self.assertTrue(all(df_no_outliers["A"] < threshold))
