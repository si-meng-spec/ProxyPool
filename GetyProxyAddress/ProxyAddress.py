from Request import MyRequests


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
        self.request = MyRequests().sendRequestText

    #   获取云代理网站上的公开代理
    def crawl_ip3366(self, page_count=4):
        for style in range(1, 3):
            for url in [f"http://www.ip3366.net/free/?stype={style}&page={count}" for count in
                        range(1, page_count + 1)]:
                for inf in self.Template1(url):
                    yield inf

    #   获取89ip上的公开代理
    def crawl_Pool89ip(self, page_count=8):
        for url in [f"https://proxy.ip3366.net/free/?action=china&page={count}" for count in range(1, page_count + 1)]:
            for inf in self.Template1(url):
                yield inf
