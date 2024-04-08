import pandas as pd


class DFProcessor:
    """
    A class to process dataframes
    """

    def __init__(self):
        pass

    @staticmethod
    def drop_outliers(df: pd.DataFrame, column: str, threshold: float) -> pd.DataFrame:
        """
        Drop outliers in a dataframe.
        :param df: The dataframe.
        :param column: The column to drop outliers.
        :param threshold: The threshold to consider as an outlier.
        :return: pd.DataFrame: The dataframe without outliers.
        """
        return df[(df[column] < threshold)]
