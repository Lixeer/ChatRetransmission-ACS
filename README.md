# ChatRetransmission-ACS
![](https://github.com/Lixeer/ChatRetransmission-ACS/blob/main/resource/qxlarge-dsc-375E24F76A8D07723A207852AA5C313D_1.jpg)
## 这是嘛玩应
基于python实现的chatgpt上下文代理异步镜像服务端1.2.0
## 效果图

![](https://github.com/Lixeer/ChatRetransmission-ACS/blob/main/resource/7Y0TWN%60IBK%7EGOSQT3GDTS3.png)
__作者是真IKUN__
![](https://github.com/Lixeer/ChatRetransmission-ACS/blob/main/resource/BXCLWG%25W%405%7D%7D0GO%7DRIEQPE0.png)
![](https://github.com/Lixeer/ChatRetransmission-ACS/blob/main/resource/U%5D1781U%2560VX00KKHST%24MH4.png)
## 食用方法
ACS-main.py文件在服务端部署，默认端口：5702（一般不会冲突，冲突修改就行 冲突请修改config.py）

#### 1.修改配置文件
```python
#config.py
PORT = 5702 #服务端启动端口
RedisPORT = 1337 #Redis数据库监听端口
```
#### 2.更新Centos软件包
```bash
sudo yum update
```

#### 3.安装Redis
```bash
sudo yum update
```
#### 4.修改redis配置文件
```bash
sudo vi /etc/redis.conf
```
将
```
daemonize no
//中间省略一大部分
port 6379 //此处为redis默认启动端口
```
修改为
```
daemonize yes //后台运行
//中间省略一大部分
port 1337  //此处为redis默认启动端口
```

```
python ACS-main.py
```
#### 5.启动redis
```bash
redis-server
```
#### 6.安装python依赖(有宝塔直接跳过这步)
```bash
pip install -r requirements.txt
```
#### 7.启动服务端
```bash
python ACS-main.py
```

服务端建议选择境外服务器的最低配置即可。  
此项目对内存要求极低 运行7*24小时不到30m 几乎不在服务端储存会话

## TODO
- [ ] 请求冷却系统
- [ ] 客户端代理(组件API)
- [x] 高性能异步请求
- [x] DB实现key请求  

## 更新修复
- [x] 修复了aiohttp框架下长连接报错问题
- [x] 更换了性能更高，开发更容易的fastapi-web框架
- [x] 实现了一个key绑定一个电脑
- [x] 使用了轻量级高性能数据库组件-Redis
- [ ] 请求太多时 由于openai限制会直接熄火的问题（资金有限直接摆烂不解决了） 


## 设计-UML图
空白



##
有bug希望及时反馈。  
ChatGPT免费体验群738104595  
群内内置机器人 带有ai画图各种功能  
感谢支持


