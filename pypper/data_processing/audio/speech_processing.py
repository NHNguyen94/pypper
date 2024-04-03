from typing import Iterable
from typing import Optional, Dict

from faster_whisper import WhisperModel

from pypper.utils.enums import SpeechProcessingConfigs


class SpeechProcessor:
    """
    A class to process speech to text
    """

    def __init__(
        self,
        model_size: Optional[str] = None,
        device: Optional[str] = None,
        compute_type: Optional[str] = None,
    ):
        self.configs = SpeechProcessingConfigs()
        if model_size is None:
            self.model_size = self.configs.DEFAULT_MODEL
        else:
            self.model_size = model_size
        if device is None:
            self.device = self.configs.DEFAULT_DEVICE
        else:
            self.device = device
        if compute_type is None:
            self.compute_type = self.configs.DEFAUL_COMPUTE_TYPE
        else:
            self.compute_type = compute_type
        self.whisper_model = WhisperModel(
            model_size_or_path=self.model_size,
            device=self.device,
            compute_type=compute_type,
        )

    def construct_response(self, segments: Iterable):
        """
        Construct a response from the segments
        :param segments: Iterable: The segments returned from the model
        :return: str: The response
        """
        response = ""
        for segment in segments:
            response += segment.text + " "
        return response

    def speech_to_text(
        self,
        audio_path: str,
        language: Optional[str],
        beam_size: Optional[int] = None,
    ) -> (str, Dict):
        """
        Convert speech to text
        :param audio_path: str: The path to the audio file
        :param language: str: The language of the audio
        :param beam_size: int: The beam size
        :return: str: The response in text
        """
        segments, metadata = self.whisper_model.transcribe(
            audio=audio_path,
            beam_size=beam_size,
            language=language,
        )
        response = self.construct_response(segments=segments)
        return response, metadata
