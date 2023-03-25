import requests

import json
def userMsgCreat(msg:str) -> dict:
    '''
    msg:���ڹ����û��ظ�����
    '''
    #�û���Ϣ����
    return {"role": "user", "content": msg}


def aiMsgCreat(msg:str) -> dict:
    '''
    msg:���ڹ���ai�ظ�����
    '''
    #ai��Ϣ����
    return {"role": "assistant", "content": msg}

def get_chat(msg:list) -> str:
    """
    msg����¼��������Ϣ
    """
    url = "http://127.0.0.1:5701/chat"  #url���������������߹���IP


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
        print("������")
        break
