# from unittest import TestCase
#
# from pypper.data_crawling.image_crawler import ImageCrawler
#
#
# class TestImageCrawler(TestCase):
#     def test_fetch_all_and_save(self):
#         print("Test function fetch_all_and_save")
#         crawler = ImageCrawler()
#         url_list = [
#             "https://pokemon.fandom.com/vi/wiki/Th%E1%BB%83_lo%E1%BA%A1i:Pok%C3%A9mon"
#         ]
#         # Should run without error
#         crawler.fetch_all_and_save(url_list=url_list,
#                                    substring_condition=["pokemon"],
#                                    endswith_condition=("vi", "png", "jpg"),
#                                    output_csv_file_path="test/output_for_tests/test_images.csv",
#                                    )
