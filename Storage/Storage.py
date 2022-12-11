import json
import random
import os, sys

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from Ver import Verification


class IPProxyStorage:
    def __init__(self):
        self.__data = {"https": [], "http": []}
        self.ver = Verification()
        self.folder_name = os.path.dirname(os.path.realpath(__file__))

    def get(self, accord: str = "http") -> str or None:
        accord = accord.lower()
        if accord in ['https', 'http'] and len(self.__data[accord]) != 0:
            return random.choice(self.__data[accord])
        return None

    def add(self, accord: str, ip_port: str) -> bool:
        accord = accord.lower()
        if accord in ['https', 'http']:
            self.__data[accord].append(ip_port)
            return True
        return False

    def count(self):
        return {'https': len(self.__data['https']), 'http': len(self.__data['http'])}

    def all(self):
        return self.__data[:]

    def verip(self):
        self.__data = self.ver.run(self.__data[:])


if __name__ == "__main__":
    storage = IPProxyStorage()
    storage.verip()
