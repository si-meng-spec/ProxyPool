import sys
import requests


class Verification:
    def __init__(self):
        self.request = requests.get

    def verifyip(self, accord: str, ip_port: str):
        url = "http://icanhazip.com/" if accord == "HTTP" else "https://icanhazip.com/"
        if accord.lower() in ['http', 'https']:
            try:
                res = self.request(url=url, proxies={accord.lower(): ip_port}, timeout=3).text
            except:
                return None
            return res
