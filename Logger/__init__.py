import os
import sys
import time
sys.path.append(os.path.dirname(os.getcwd()))
from utils import singleton

@singleton
class LogManager:
    def __init__(self, showlog=False):
        self.name = "Logger"
        self.showlog = showlog
        self.log_path = ""
        #   获取当前文件所在文件夹的绝对路径
        self.folder_name = os.path.dirname(os.path.realpath(__file__))
        self.filename = f"{time.strftime(f'%Y-%m-%d %H-%M-%S', time.localtime())}.log"
        self.count = 0
        self.fp = sys.stdout if showlog else open(f"{self.folder_name}\\log\\{self.filename}", 'w', encoding='utf-8')

    # 记录对应日志
    def log(self, name, content):
        self.fp.write(f"{time.strftime(f'[%Y-%m-%d %H:%M:%S]', time.localtime())}[{name}]:{content}\n")
        if not self.showlog:
            self.fp.close()
            self.fp = open(f"{self.folder_name}\\log\\{self.filename}", 'a', encoding='utf-8')
        self.count += 1

    def clearlog(self):
        for filename in os.listdir(f"{self.folder_name}\\log\\"):
            if filename.split(".")[-1] == "log" and filename != self.filename:
                os.remove(f"{self.folder_name}\\log\\{filename}")

    def __del__(self):
        if self.count > 0 and not self.showlog:
            print(f"当前日志文件被保存在：{self.folder_name}\\{self.filename}")
