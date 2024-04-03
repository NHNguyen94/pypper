from typing import List, Dict, BinaryIO

from pypdf import PdfReader

from pypper.utils.enums import PDFDocumentConfigs


class PDFHandler:
    """
    A class to read PDF files
    """

    def __init__(self):
        self.configs = PDFDocumentConfigs()

    def _create_pdf_object(self, file: BinaryIO) -> PdfReader:
        """
        Create a PDF object
        :param file: BinaryIO: The PDF file
        :return: PdfReader: The PDF object
        """
        return PdfReader(file)

    def _get_num_pages(self, pdf_reader: PdfReader) -> int:
        """
        Get the number of pages in the PDF document
        :param pdf_reader: PdfReader: The PDF object
        :return: int: The number of pages in the PDF document
        """
        return len(pdf_reader.pages)

    def _extract_text(self, page_number: int, pdf_reader: PdfReader) -> str:
        """
        Extract the text from a page
        :param page_number: int: The page number
        :param pdf_reader: PdfReader: The PDF object
        :return: str: The text from the page
        """
        return pdf_reader.pages[page_number].extract_text()

    def _get_page_label(self, page_number: int, pdf_reader: PdfReader) -> str:
        """
        Get the label of a page
        :param page_number: int: The page number
        :param pdf_reader: PdfReader: The PDF object
        :return: str: The label of the page
        """
        return pdf_reader.page_labels[page_number]

    def _generate_document(
        self, page_number: int, page_label: str, page_text: str
    ) -> Dict:
        """
        Generate a document
        :param page_number: int: The page number
        :param page_label: str: The page label
        :param page_text: str: The page text
        :return: Dict:
            A dictionary containing the page number, page label, and page text
        """
        return {
            self.configs.PAGE: page_number,
            self.configs.PAGE_LABEL: page_label,
            self.configs.PAGE_TEXT: page_text,
        }

    def load_single_pdf_file(
        self,
        file_path: str,
    ) -> List[Dict]:
        """
        Load the data from a PDF file
        :param file_path: str: The path to the PDF file
        :return: List[Dict]: A list of dictionaries containing the page number,
        page label,
        and page text
        """
        with open(file_path, "rb") as file:
            pdf = self._create_pdf_object(file)
            num_pages = self._get_num_pages(pdf)
            docs = []
            for page in range(num_pages):
                page_text = self._extract_text(page, pdf)
                page_label = self._get_page_label(page, pdf)
                doc = self._generate_document(page, page_label, page_text)
                docs.append(doc)
        return docs
