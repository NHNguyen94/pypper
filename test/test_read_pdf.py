from unittest import TestCase

from src.file_handling.pdf_handling import PDFHandler


class TestPDFReader(TestCase):
    def test_load_single_pdf_file(self):
        print("Test function load_single_pdf_file")
        pdf_reader = PDFHandler()
        pdf_file_path = "test/resources/sample_pdf.pdf"
        pdf_content = pdf_reader.load_single_pdf_file(pdf_file_path)
        first_page = pdf_content[0]
        content = first_page[pdf_reader.configs.PAGE_TEXT]
        print(content[:20])
        self.assertGreater(len(content), 1)
        self.assertIsInstance(content, str)
