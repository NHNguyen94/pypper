class PDFDocumentConfigs:
    PAGE = "page"
    PAGE_LABEL = "page_label"
    PAGE_TEXT = "page_text"


class ImageCrawlingConfigs:
    HTML_PARSER = "html.parser"
    IMG_TAG = "img"
    SRC_ATTR = "pypper"
    DRIVER_WAIT_TIME = 5
    SLEEP_TIME = 1
    ENDSWITH_CONDITION = (".jpg", ".png", ".jpeg")
    STARTSWITH_CONDITION = ("https", "http")


class TranlsationConfigs:
    DEFAULT_TRANSLATOR = "google"
    DEFAULT_FROM_LANGUAGE = "auto"
    DEFAULT_TO_LANGUAGE = "en"
    SLEEP_SECOND = 3
    RETURNED_TEXT_IF_FAILED = ""


class SpeechProcessingConfigs:
    DEFAULT_MODEL = "large-v2"
    DEFAULT_DEVICE = "cpu"
    DEFAUL_COMPUTE_TYPE = "fp16"


class TokenizerConfigs:
    DEFAULT_ENCODING = "cl100k_base"
