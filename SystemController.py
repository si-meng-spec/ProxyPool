import asyncio
import random
import time
from GetyProxyAddress import ProxyAddressPool
from Storage import IPProxyStorage
from Ver import Verification

storage = IPProxyStorage()
proxy = ProxyAddressPool()
verification = Verification()
for func in proxy.__CrawlFunc__:
    for inf in eval(f"proxy.{func}()"):
        storage.add(inf[0], inf[1])

print(storage.count())
verification.run()
print("可用代理：")
print(storage.count())
print(storage.all())