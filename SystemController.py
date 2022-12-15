from Logger import LogManager
from GetyProxyAddress import ProxyAddressPool
from Storage import IPProxyStorage, SocketServer
from Ver import Verification
import time

# 日志管理器
Log_Manager = LogManager(save_log=True)
Log_Manager.clear_log()
# 爬虫管理器
Proxy_Pool = ProxyAddressPool()
# IP地址存储器
Storage = IPProxyStorage()
# 验证IP可用管理器
verification = Verification()

# Socket服务器IP地址
socket_ip = "127.0.0.1"
# Socket服务器端口
socket_accord = 8585

# Socket服务管理器
Socket_Server = SocketServer(socket_ip, socket_accord)

Log_Manager.log("SYS", "程序启动中...")
Log_Manager.log("SYS", "正在获取网上代理...")
# 调用爬虫函数,从网上获取免费代理IP,并添加到IP存储库中
for CrawlFunc in Proxy_Pool.__CrawlFunc__:
    for inf in eval(f"Proxy_Pool.{CrawlFunc}()"):
        Storage.add(accord=inf[0], ip_port=inf[1])

# 验证IP代理
Log_Manager.log("SYS", "正在验证IP")
verification.run()
ip_count = Storage.count()
Log_Manager.log("SYS", f"可用HTTP代理IP数量有：{ip_count['http']}")
Log_Manager.log("SYS", f"可用HTTPS代理IP数量有：{ip_count['https']}")
# 开启Socket服务
Log_Manager.log("SYS", f"正在开启Socket服务,IP地址为{socket_ip}:{socket_accord}")
Socket_Server.run()
# 每隔半小时验证一次
while True:
    time.sleep(60 * 30)
    Log_Manager.log("SYS", "正在验证IP")
    verification.run()
