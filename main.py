from GetyProxyAddress import ProxyAddressPool
from Ver import Verification

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
}
ver = Verification()
proxy = ProxyAddressPool()
for fun in proxy.__CrawlFunc__:
    for inf in eval(f"proxy.{fun}()"):
        data = ver.verifyip(accord=inf[0], ip_port=inf[1])
        if data is None:
            print(f"{inf[0]}://{inf[1]} 代理使用失败！")
        else:
            print(f"{inf[0]}://{inf[1]} 代理使用成功！！！")
            print(data)
