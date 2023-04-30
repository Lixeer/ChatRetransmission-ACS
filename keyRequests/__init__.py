from abc import ABC,abstractmethod

import redis

import config

class WrongMac(ValueError):
    def __init__(self, message="错误的Mac 该key已经被绑定过"):
        self.message = message




class AbckeyRequests(ABC):
    """
    抽象key基类
    """
    @abstractmethod
    def isPass(self,key:str):
        raise NotImplementedError

    def __call__(self,key:str,mac:str):
        return self.isPass(key=key,mac=mac)

class keyTs(AbckeyRequests):
    """
    测试用
    """
    def isPass(self,key) -> bool:
        print(key)
        return True
    @abstractmethod
    def __call__(self,key:str,mac):
        pass

class FileKey(AbckeyRequests):



    def __init__(self,filePath:str):
        self.path=filePath


    def isPass(self,key:str,mac:str)-> bool:
        with open(self.path) as file:
            keyPool=[line.replace("\n","") for line in file]
        #print(keyPool)
        if key in keyPool:
            return True
        else:
            return False

class RedisDBKey(AbckeyRequests):
    def __init__(self,DBport=config.RedisPORT,DBip="127.0.0.1"):

        """
        :param DBip:数据库地址
        :param DBport:数据库端口
        """

        self.port = DBport
        self.ip = DBip
        self.redis=redis.Redis(host=self.ip,port=self.port)
    def isPass(self,key:str,mac:str):
        """

        :param key:请求的key
        :param mac: 客户端物理地址
        :return: 是否通过

        """
        result=self.redis.get(key).decode("utf-8") #一点小坑
        if result == mac:
            return True
        elif result == config.placeholder:
            self.redis.set(key,mac)

            return True
        elif result != None and result != mac:
            raise WrongMac()
        else:
            return False
    def creatNewKey(self,key:str)->bool:
        """

        :param key: 欲要创建的key
        :return:是否成功

        """
        try:
            self.redis.set(key, config.placeholder)
            return True
        except:
            return False





class MySQLDBKey(AbckeyRequests):
    pass

class JsonKey(FileKey):
    def isPass(self,key:str,mac:str)->bool:
        pass

def keyRequestFactory():
    print("[输入key储存方案]\n1.本地txt文件储存key(出现文件锁问题)\n2.Redis中间件数据库储存key\n3.Mysql中间件数据库储存\n4.本地json文件储存key")  #不合理的设计 在包中加入了脚本代码
    print(f"已选择[{config.KETSRTATE}]")
    c=config.KETSRTATE
    if c == "1":
        return FileKey(filePath="keyRequests/key.txt")
    elif c == "2":
        return RedisDBKey()
    elif c == "3":
        return MySQLDBKey()
    elif c== "4":
        return  JsonKey(filePath="keyRequests/key.json")

keyControl=keyRequestFactory()

'''
r=RedisDBKey()
r(key="1233",mac="12544")
'''