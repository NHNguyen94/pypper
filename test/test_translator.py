from unittest import TestCase
import pandas as pd
from src.data_processing.text.translation import Translator


class TestTranslator(TestCase):
    def test_translate_in_df(self):
        print("Test function translate_in_df")
        translator = Translator(from_language="en", to_language="vi")
        df = pd.DataFrame({"text": ["hello", "hi"]})
        df = translator.translate_in_df(df=df, column_to_translate="text", column_to_store="translated_text")
        df['translated_text'] = df['translated_text'].str.lower()
        print(df)
        self.assertTrue("chào" in df['translated_text'].values)

