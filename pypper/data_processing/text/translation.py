import time
from typing import Optional

import pandas as pd
import translators as ts

from pypper.utils.enums import TranlsationConfigs


class Translator:
    """
    A class to translate text
    """

    def __init__(
        self,
        from_language: Optional[str] = None,
        to_language: Optional[str] = None,
        translator: Optional[str] = None,
    ):
        """
        Initialize the Translator object
        :param from_language:
            The language to translate from,
            if None, the language will be detected automatically
        :param to_language:
            The language to translate to, if None, it will be "en"
        :param translator:
            The translator to use
        """
        self.configs = TranlsationConfigs()
        if translator is None:
            self.translator = TranlsationConfigs().DEFAULT_TRANSLATOR
        else:
            self.translator = translator
        if from_language is None:
            self.from_language = TranlsationConfigs().DEFAULT_FROM_LANGUAGE
        else:
            self.from_language = from_language
        if to_language is None:
            self.to_language = TranlsationConfigs().DEFAULT_TO_LANGUAGE
        else:
            self.to_language = to_language

    def translate_text(
        self, text: str, returned_text_if_failed: Optional[str] = ""
    ) -> str:
        """
        Translate text
        :param text: The text to translate
        :param returned_text_if_failed:
            The text to return if the translation fails
        :return: str: The translated text
        """
        try:
            return ts.translate_text(
                query_text=text,
                from_language=self.from_language,
                to_language=self.to_language,
                translator=self.translator,
            )
        except Exception as e:
            print(f"Failed to translate text: {e}")
            return returned_text_if_failed

    def translate_in_df(
        self,
        df: pd.DataFrame,
        column_to_translate: str,
        column_to_store: str,
        stop_index: Optional[int] = None,
        sleep_second: Optional[int] = None,
        returned_text_if_failed: Optional[str] = "",
    ):
        """
        Translate text in a DataFrame
        :param df:
            DataFrame with the column to translate
        :param column_to_translate:
            The column to translate
        :param column_to_store:
            The column to store the translated text
        :param stop_index:
            The index to stop translating
        :param sleep_second:
            The time to sleep between translations
        :param returned_text_if_failed:
            The text to return if the translation fails
        :return:
        """
        if stop_index is None:
            stop_index = len(df)
        if sleep_second is None:
            sleep_second = self.configs.SLEEP_SECOND
        n = 0
        for row in df[column_to_translate]:
            df[column_to_store] = self.translate_text(
                text=row, returned_text_if_failed=returned_text_if_failed
            )
            n += 1
            time.sleep(sleep_second)
            if n > stop_index:
                break
        return df
