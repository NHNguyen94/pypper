from typing import List
from unittest import TestCase

from pypper.data_processing.nlp.tokenizing import Tokenizer


class TestTokenizer(TestCase):
    def test_encode_text(self):
        print("Test function encode_text")
        tokenizer = Tokenizer()
        text = "This is a test sentence."
        tokens = tokenizer.encode_text(text)
        print(tokens)
        self.assertGreater(len(tokens), 1)
        self.assertIsInstance(tokens, List)

    def test_decode_tokens(self):
        print("Test function decode_tokens")
        tokenizer = Tokenizer()
        encoded_text = [2028, 374, 264, 1296, 11914, 13]
        text = tokenizer.decode_tokens(encoded_text)
        print(text)
        self.assertGreater(len(text), 1)
        self.assertIsInstance(text, str)
