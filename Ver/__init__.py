import aiohttp
import requests
import os
import sys
import asyncio
from concurrent.futures import ThreadPoolExecutor

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from Storage import IPProxyStorage


class Verification:
    def __init__(self):
        self.storage = IPProxyStorage()
        self.request = requests.get

    async def http(self, ip_port: str) -> None:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("http://icanhazip.com/", proxy=f'http://{ip_port}', timeout=10) as resp:
                    if resp.status != 200:
                        self.storage.remove('http', ip_port)
        except:
            self.storage.remove('http', ip_port)

    def https(self, ip_port) -> None:
        try:
            res = self.request("https://icanhazip.com/", proxies={'https': f'https://{ip_port}'}, timeout=10)
        except:
            self.storage.remove('https', ip_port)

    def run(self) -> None:
        # 验证HTTP代理
        async def main():
            func_list = [asyncio.create_task(self.http(ip_port)) for ip_port in self.storage.all()['http']]
            for func in func_list:
                await func

        loop = asyncio.new_event_loop()
        loop.run_until_complete(main())

        # 验证HTTPS代理
        theard_pool = ThreadPoolExecutor(max_workers=60)
        for ip in self.storage.all()['https']:
            theard_pool.submit(self.https, ip)
        theard_pool.shutdown(wait=True)
