import os
import random
import sys
import time

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from utils import singleton


@singleton
class IPProxyStorage:
    def __init__(self):
        self.__data = {"https": [], "http": []}
        folder_path = os.path.abspath(os.path.dirname(os.getcwd()))
        with open(f"{folder_path}\\data\\http_proxies.txt", 'r', encoding='utf-8') as f:
            for line in f.read().split("\n"):
                self.__data['http'].append(line)
        with open(f"{folder_path}\\data\\https_proxies.txt", 'r', encoding='utf-8') as f:
            for line in f.read().split("\n"):
                self.__data['https'].append(line)

    def get(self, accord: str = "http") -> str or None:
        accord = accord.lower()
        if accord in ['https', 'http'] and len(self.__data[accord]) != 0:
            return random.choice(self.__data[accord])
        return None

    def add(self, accord: str, ip_port: str) -> bool:
        accord = accord.lower()
        if accord in ['https', 'http']:
            if ip_port not in self.__data[accord]:
                self.__data[accord].append(ip_port)
            return True
        return False

    def remove(self, accord: str, ip_port: str) -> bool:
        accord = accord.lower()
        if accord not in ['https', 'http']:
            return False
        data = self.__data[accord].copy()
        for inf in data:
            if ip_port == inf:
                self.__data[accord].remove(ip_port)
                return True
        return False

    def count(self):
        return {'https': len(self.__data['https']), 'http': len(self.__data['http'])}

    def all(self):
        return self.__data.copy()
