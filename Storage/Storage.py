import json
import random
import os


class IPProxyStorage:
    def __init__(self):
        self.__data = {"https": [], "http": []}
        self.folder_name = os.path.dirname(os.path.realpath(__file__))

    def get_ip(self, accord: str = "http") -> str or None:
        accord = accord.lower()
        if accord in ['https', 'http'] and len(self.__data[accord]) != 0:
            return random.choice(self.__data[accord])
        return None

    def add_ip(self, accord: str, ip_port: str) -> bool:
        accord = accord.lower()
        if accord in ['https', 'http']:
            self.__data[accord].append(ip_port)
            return True
        return False

    def save(self):
        with open(f"{self.folder_name}\\data.json", 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.__data, indent=2))


if __name__ == "__main__":
    storage = IPProxyStorage()
    storage.save()
