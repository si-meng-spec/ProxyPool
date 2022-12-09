from typing import Dict, Any

import requests
from requests.exceptions import *


class MyRequests:
    def __init__(self, headers=None, encoding: str = "", proxies=None, timeout: int = 5, verify: bool = False):
        # __init__ 用以配置插件
        if headers is None:
            headers = {}
        if proxies is None:
            proxies = {}
        self.session = requests.session()  # 维持会话
        self.headers = headers
        self.encoding = encoding
        self.proxies = proxies
        self.timeout = timeout
        self.verify = verify
        if not self.verify:
            requests.packages.urllib3.disable_warnings()  # 关闭SSL不信任提示

    '''
    URL     访问连接
    data    参数
    method  访问方法,默认GET
    '''

    def __sendrequest(self, url: str, data: Dict[Any, Any] = {}, method="GET", *args, **kw):
        try:
            response = self.session.request(url=url, method=method, headers=self.headers, data=data,
                                            proxies=self.proxies, verify=self.verify, timeout=self.timeout, *args, **kw)
        except ReadTimeout as e:
            return None
        except ConnectionError as e:
            return None
        except RequestException as e:
            return None
        return response

    '''
    发送请求并返回二进制值
    '''

    def sendRequestBin(self, url: str, data: Dict[Any, Any] = {}, method="GET", *args, **kw):
        res = self.__sendrequest(
            url=url, data=data, method=method, *args, **kw)
        if res is not None:
            return res.content
        return res

    '''
    发送请求并返回文字
    '''

    def sendRequestText(self, url: str, data: Dict[Any, Any] = {}, method="GET", encoding="", *args, **kw):
        res = self.__sendrequest(
            url=url, data=data, method=method, *args, **kw)
        if res is not None:
            res.encoding = self.encoding if encoding == "" else encoding
            return res.text
        return None
