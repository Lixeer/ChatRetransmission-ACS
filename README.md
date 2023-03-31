# ChatRetransmission-ACS

## 这是嘛玩应
基于python实现的chatgpt上下文代理异步镜像服务端1.2.0
## 效果图

![](https://github.com/Lixeer/ChatRetransmission-ACS/blob/main/resource/7Y0TWN%60IBK%7EGOSQT3GDTS3.png)
__作者是真IKUN__
![](https://github.com/Lixeer/ChatRetransmission-ACS/blob/main/resource/BXCLWG%25W%405%7D%7D0GO%7DRIEQPE0.png)
![](https://github.com/Lixeer/ChatRetransmission-ACS/blob/main/resource/U%5D1781U%2560VX00KKHST%24MH4.png)
## 食用方法
ACS-main.py文件在服务端部署，默认端口：5702（一般不会冲突，冲突修改就行 冲突请修改config.py）。
```python
#config.py
PORT=5702 #修改这一行
```
```
python ACS-main.py
```
即可

client.py文件在本地可以直接使用，但是需要配置好服务端。在url中填入正确的服务端域名或者IP。

服务端建议选择国外vps的最低配置即可。
此项目对内存要求极低 运行7*24小时不到30m 几乎不在服务端储存会话

## TODO
- [ ] 请求冷却系统
- [ ] 客户端代理(组件API)
- [x] 高性能异步请求
- [ ] DB实现key请求


有bug希望及时反馈。
感谢  https://github.com/cfwasd/ChatRetransmission-ACS 
的帮助

