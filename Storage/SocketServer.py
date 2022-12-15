import socket
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from Logger import LogManager
from Storage import IPProxyStorage


class SocketServer:
    def __init__(self, ip:str, port:int):
        self.s = socket.socket()
        self.s.bind((ip, port))
        self.s.listen()
        self.Log_manager = LogManager()
        self.proxy = IPProxyStorage()
        self.ip_port = f"{ip}:{port}"

    def run(self):
        self.Log_manager.log("SocketServer", f"已开启Socket服务,访问 {self.ip_port}/http 可以获取HTTP代理")
        self.Log_manager.log("SocketServer", f"已开启Socket服务,访问 {self.ip_port}/https 可以获取HTTPS代理")
        while True:
            client, address = self.s.accept()
            # 只获取请求头的第一行,进行解析
            data = client.recv(1024).decode('utf-8').split("\n")[0].replace("\r", "").split(" ")
            if data[0] == 'GET' or data[0] == 'POST':
                res = self.proxy.get(data[1][1:])
                res = res if res is not None else ""
                self.Log_manager.log("SocketServer",
                                     f"客户机地址:{address[0]}:{address[1]},服务器地址:{self.ip_port},请求数据:{data[1][1:]},回应数据:{res}")
                client.send(f'HTTP/1.1 200 OK\r\n\r\n{res}'.encode('utf-8'))
                client.close()
