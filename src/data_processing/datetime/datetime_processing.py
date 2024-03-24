from datetime import datetime

class DateTimeProcessor():
    def __init__(self):
        pass

    @staticmethod
    def get_current_utc_timestamp() -> str:
        current_timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        return current_timestamp

    @staticmethod
    def get_current_local_timestamp() -> str:
        current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return current_timestamp