from typing import Optional, List

import tiktoken as tk

from pypper.utils.enums import TokenizerConfigs


class Tokenizer:
    """
    A class to tokenize text.
    """

    def __init__(self, encoding_name: Optional[str] = None):
        """
        Initialize the Tokenizer object.
        :param encoding_name: Name of the encoding to use.
        """
        self.configs = TokenizerConfigs()
        if encoding_name is None:
            self.encoder = tk.get_encoding(self.configs.DEFAULT_ENCODING)
        else:
            self.encoder = tk.get_encoding(encoding_name)

    def encode_text(self, text: str) -> List:
        """
        Encode a text into tokens.
        :param text: Text to tokenize.
        :return: List of tokens.
        """
        tokens = self.encoder.encode(text)
        return tokens

    def count_tokens(self, text: str) -> int:
        """
        Count the number of tokens in a text.
        :param text: Text to tokenize.
        :return: Number of tokens.
        """
        tokens = self.encode_text(text)
        return len(tokens)

    def decode_tokens(self, tokens: List) -> str:
        """
        Decode tokens into text.
        :param tokens: Tokens to decode.
        :return: Decoded text.
        """
        return self.encoder.decode(tokens)
