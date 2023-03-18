#coding:gbk
import requests
from typing import List
import json
def userMsgCreat(msg:str) -> dict:
    return {"role": "user", "content": msg}

def aiMsgCreat(msg:str) -> dict:
    return {"role": "assistant", "content": msg}

def get_chat(msg:list) -> str:
    url = "http://104.168.136.237:5701/chat2"


    data = {"msg": msg}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()['choices'][-1]['message']['content']
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
        print("出错辣")
        break
