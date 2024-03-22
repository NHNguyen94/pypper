class PDFDocumentConfigs():
    PAGE = "page"
    PAGE_LABEL = "page_label"
    PAGE_TEXT = "page_text"

class ImageCrawlingConfigs():
    HTML_PARSER = "html.parser"
    IMG_TAG = "img"
    SRC_ATTR = "src"
    DRIVER_WAIT_TIME = 5
    SLEEP_TIME = 1
    ENDSWITH_CONDITION = (".jpg", ".png", ".jpeg")
    STARTSWITH_CONDITION = ("https", "http")

class TranlsationConfigs():
    DEFAULT_TRANSLATOR = "google"
    SLEEP_SECOND = 3
    RETURNED_TEXT_IF_FAILED = ""