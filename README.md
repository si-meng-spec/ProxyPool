# ProxyPool

一个简易的代理池，提供如下功能：

- 每次启动的时候抓取免费代理网站，简易可扩展。
- 每半小时进行一次测试和筛选，剔除不可用代理，留下可用代理。
- 提供代理 API，随机取用测试通过的HTTP/HTTPS可用代理。

代理池的具体结构参考自 https://github.com/Python3WebSpider/ProxyPool

## 使用方法
下载完 requirements.txt 中的模块
```
pip install -r requirements.txt
```
然后运行SystemController.py

运行结果应该如下

```
[2022-12-15 22:19:01][SYS]:程序启动中...
[2022-12-15 22:19:01][SYS]:正在获取网上代理...
[2022-12-15 22:19:08][SYS]:正在验证IP
[2022-12-15 22:19:29][SYS]:可用HTTP代理IP数量有：282
[2022-12-15 22:19:29][SYS]:可用HTTPS代理IP数量有：0
[2022-12-15 22:19:29][SYS]:正在开启Socket服务,IP地址为127.0.0.1:8585
[2022-12-15 22:19:29][SocketServer]:已开启Socket服务,访问 127.0.0.1:8585/http 可以获取HTTP代理
[2022-12-15 22:19:29][SocketServer]:已开启Socket服务,访问 127.0.0.1:8585/https 可以获取HTTPS代理
```

这个时候访问[http://localhost:8585/http](http://localhost:8585/http)和[http://localhost:8585/https](http://localhost:8585/https)
即可获得对应的代理,每次会从当前可用的代理中随机返回一个

## 可配置项
在SystemController.py中,可用配置Socket监听的端口

在data文件夹下存放http_proxies.txt和https_proxies.txt,可用添加已知的可用代理,会自动导入的

## 程序结构
```commandline
├─data                      #   存放数据的文件夹
│  ├─http_proxies.txt       #   存在HTTP代理
│  ├─https_proxies.txt      #   存放HTTPS代理
├─GetProxyAddress           #   爬虫
│  ├─__init__.py
│  └─ProxyAddress.py        #   从公开免费代理网站上获取代理IP
├─Logger
│  ├─__init__.py            #   日志文件并保存
│  ├─log                    #   存放日志文件
├─Storage
│  ├─__init__.py
│  ├─IPStorage.py           #   存放IP代理
│  ├─SocketServer.py        #   通过Socket监听端口并返回信息
├─Ver
│  ├─__init__.py            #   验证代理是否可用
├─README.md
├─requirements.txt
├─SystemController.py       #   调用各个模块
├─utils.py
```
## 扩展代理爬虫

代理的爬虫均放置在 proxypool/GetProxyAddress/ProxyAddress.py 文件内下，目前对接了有限几个代理的爬虫。
后面会要是遇到了有免费代理IP也会加上去。

如果要扩展一个爬虫,只需要再ProxyAddress.py的ProxyAddressPool类中,再添加一个函数,函数名以crawl_开头,并且返回值的格式为
[协议:IP:端口]即可，例['http','127.0.0.1:80']

## 已有对应爬虫的网站
注:只获取了对应网站的免费代理
- 齐云代理:[https://proxy.ip3366.net/](https://proxy.ip3366.net/)
- 开心代理:[http://www.kxdaili.com/dailiip.html](http://www.kxdaili.com/dailiip.html)

## 推荐两个国外的免费的代理IP的网站
本项目的 http_proxies.txt 也是由这两个网站提供的。
- ProxyScrape：[https://proxyscrape.com/free-proxy-list](https://proxyscrape.com/free-proxy-list)
- Open Proxy Space：[https://openproxy.space/list/http](https://openproxy.space/list/http)

## 参考内容
- 项目：[https://github.com/Python3WebSpider/ProxyPool](https://github.com/Python3WebSpider/ProxyPool)
- 文章：[如何搭建一个高效的代理池](https://cuiqingcai.com/7048.html)

