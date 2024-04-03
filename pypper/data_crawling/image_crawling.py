import time
from typing import List, Tuple, Optional

from bs4 import BeautifulSoup
from selenium import webdriver

from pypper.data_crawling.base_crawling import BaseCrawler
from pypper.file_handling.csv_handling import CSVHandler
from pypper.utils.enums import ImageCrawlingConfigs


class ImageCrawler(BaseCrawler):
    """
    A class to crawl images from urls
    """

    def __init__(self):
        super().__init__()
        self.csv_handler = CSVHandler()
        self.configs = ImageCrawlingConfigs()

    def fetch_one(
        self,
        url: str,
        substring_condition: List[str],
        driver: webdriver.Chrome = webdriver.Chrome(),
        endswith_condition: Optional[Tuple[str, ...]] = None,
        startswith_condition: Optional[Tuple[str, ...]] = None,
        driver_wait_time: Optional[int] = None,
    ) -> List[str]:
        """
        Fetch image urls from a given url.
        :param url: The url to fetch image urls from.
        :param substring_condition:
            The condition that the image url should contain.
        :param driver: The webdriver object,
            you might need to download the driver
            at https://chromedriver.chromium.org/downloads
        :param endswith_condition:
            The condition that \the image url should end with.
        :param startswith_condition:
            The condition that the image url should start with.
        :param driver_wait_time:
            The time to wait for the driver to load the page.
        :return: List[str]: A list of image urls.
        """
        if endswith_condition is None:
            endswith_condition = self.configs.ENDSWITH_CONDITION
        if startswith_condition is None:
            startswith_condition = self.configs.STARTSWITH_CONDITION
        if driver_wait_time is None:
            driver_wait_time = self.configs.DRIVER_WAIT_TIME

        driver.get(url)
        try:
            driver.implicitly_wait(driver_wait_time)
            soup = BeautifulSoup(driver.page_source, self.configs.HTML_PARSER)
            image_urls = []
            for img in soup.findAll(self.configs.IMG_TAG):
                if (
                    img[self.configs.SRC_ATTR].endswith(endswith_condition)
                    and img[self.configs.SRC_ATTR].startswith(startswith_condition)
                    and any(
                        substring in img[self.configs.SRC_ATTR]
                        for substring in substring_condition
                    )
                ):
                    image_url = img[self.configs.SRC_ATTR]
                    print(f"Found image url: {image_url}")
                    image_urls.append(image_url)
            return image_urls
        except Exception as e:
            print(f"There is an error when getting image: {e}")
            return []

    def fetch_all_and_save(
        self,
        url_list: List[str],
        output_csv_file_path: str,
        substring_condition: List[str],
        driver: webdriver.Chrome = webdriver.Chrome(),
        image_url_col_name: Optional[str] = "IMAGE_URL",
        endswith_cond: Optional[Tuple[str, ...]] = None,
        startswith_cond: Optional[Tuple[str, ...]] = None,
        driver_wait_time: Optional[int] = None,
        sleep_time: Optional[float] = None,
    ) -> None:
        """
        Fetch image urls from a list of urls and save to a csv file.
        :param driver:
            The webdriver object,
            you might need to download the driver
            at https://chromedriver.chromium.org/downloads
        :param url_list: The list of urls to fetch image urls from.
        :param output_csv_file_path: The path to the output csv file.
        :param image_url_col_name:
            The name of the image url column in the output csv file.
        :param endswith_cond:
            The condition that the image url should end with.
        :param startswith_cond:
            The condition that the image url should start with.
        :param substring_condition:
            The condition that the image url should contain.
        :param driver_wait_time:
            The time to wait for the driver to load the page.
        :param sleep_time:
            The time to sleep between fetching image urls from each url.
        :return: None
        """
        if sleep_time is None:
            sleep_time = self.configs.SLEEP_TIME

        self.csv_handler.create_csv_if_not_exists(
            csv_path=output_csv_file_path, field_names=["id", image_url_col_name]
        )

        i = 0
        for url in url_list:
            image_urls = self.fetch_one(
                driver=driver,
                url=url,
                endswith_condition=endswith_cond,
                startswith_condition=startswith_cond,
                substring_condition=substring_condition,
                driver_wait_time=driver_wait_time,
            )
            for image_url in image_urls:
                self.csv_handler.append_to_csv(
                    file_path=output_csv_file_path,
                    data={"id": i, image_url_col_name: image_url},
                )
            i += 1
            time.sleep(sleep_time)

        driver.quit()
