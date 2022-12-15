import requests
from pyquery import PyQuery as pq


class ProxyMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(mcs, name, bases, attrs)


class ProxyAddressPool(object, metaclass=ProxyMetaclass):
    def __init__(self):
        self.request = requests.get

    def getHtml(self, url, encoding='utf-8'):
        try:
            res = self.request(url)
            res.encoding = encoding
        except:
            return None
        return res.text

    def crawl_proxyip3366(self, page_count=4):
        for page in range(1, page_count + 1):
            html = self.getHtml(f"https://proxy.ip3366.net/free/?action=china&page={page}")
            if html is None:
                continue
            for tr in pq(html)("table.table-bordered tr").items():
                _inf = [td.text() for td in tr.find("td").items()]
                if len(_inf) > 0 and _inf[0] != "":
                    yield [_inf[3], f"{_inf[0]}:{_inf[1]}"]

    def crawl_kxdaili(self, page_count=4):
        for x in range(1, 3):
            for y in range(1, page_count + 1):
                html = self.getHtml(f"http://www.kxdaili.com/dailiip/{x}/{y}.html")
                if html is None:
                    continue
                for tr in pq(html)("table.active tr").items():
                    _inf = [td.text() for td in tr.find("td").items()]
                    if len(_inf) > 0 and _inf[0] != "":
                        for accord in _inf[3].split(","):
                            yield [accord, f"{_inf[0]}:{_inf[1]}"]


if __name__ == "__main__":
    ProxyAddressPool = ProxyAddressPool()
    for inf in ProxyAddressPool.crawl_kxdaili():
        print(inf)
