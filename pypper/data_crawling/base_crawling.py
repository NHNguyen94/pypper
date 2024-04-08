from abc import abstractmethod, ABC


class BaseCrawler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def fetch_one(self, **kwargs):
        pass

    @abstractmethod
    def fetch_all_and_save(self, **kwargs):
        pass
