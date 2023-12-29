from datetime import datetime
from uuid import uuid4
from random import randint


class Tools:

    @staticmethod
    def getCurrentTime() -> str:
        # Get the current timestamp as a datetime object
        now = datetime.now()
        # If you want it in a specific format as a string
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
        return timestamp_str

    @staticmethod
    def generateUUID(prefixStr=None) -> str:
        if prefixStr is not None:
            return prefixStr + uuid4().hex
        return uuid4().hex

    @staticmethod
    def generateNumber(start=0, end=9, limit=5) -> str:
        random_numbers = ""
        for _ in range(limit):
            random_numbers += str(randint(start, end))
        return random_numbers
