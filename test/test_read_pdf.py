from unittest import TestCase

from pypper.util_functions.read_pdf import PDFReader


class TestPDFReader(TestCase):
    def test_load_single_pdf_file(self):
        pdf_reader = PDFReader()
        pdf_file_path = "test/resources/sample_pdf.pdf"
        pdf_content = pdf_reader.load_single_pdf_file(pdf_file_path)
        first_page = pdf_content[0]
        content = first_page[pdf_reader.configs.PAGE_TEXT]
        print(content)
        self.assertGreater(len(content), 1)
        self.assertIsInstance(content, str)
