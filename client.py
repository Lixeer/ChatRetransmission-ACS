
import requests

import json
import uuid

mac_address = ':'.join([f'{i:02x}' for i in uuid.getnode().to_bytes(6, 'big')])
def userMsgCreat(msg:str) -> dict:
    '''
    :param msg:用于构造用户回复内容
    '''
    #用户信息工厂
    return {"role": "user", "content": msg}


def aiMsgCreat(msg:str) -> dict:
    '''
    :param msg:用于构造ai回复内容
    '''
    #ai信息工厂
    return {"role": "assistant", "content": msg}

def get_chat(msg:list) -> str:
    """
    :param msg：纪录上下文信息
    """
    url = "http://address:2041/chat10"  #url填入服务端域名或者公网IP


    data = {"msg": msg,
            "key":"geluoluo",
            "mac":mac_address}
    response = requests.post(url, json=data)
    print(response.status_code)
    if response.status_code == 200:
        try:
            return response.json()['choices'][-1]['message']['content']
        except KeyError:
            return response.text
        except TypeError:
            return response.text
        #return response.text
    else:
        return "quit"
msg=[]

while True:
    iss = input()
    msg.append(userMsgCreat(iss))
    rp = get_chat(msg)
    print(rp)
    if rp != "quit":
        msg.append(aiMsgCreat(rp))
    else:
        print("出错了")
        break
