from fastapi import FastAPI, Request
import requests
import openai

import json
import datetime


import config
import keyRequests
from getChat import chat,tschat
from keyRequests import keyControl


app = FastAPI()
@app.post("/chat10")
async def handleChat(request: Request):
    data = await request.json()
    # msg = [item for item in data['msg']]
    # 不需要 decode
    msg = data['msg']
    key = data["key"]
    mac = data["mac"]
    print(keyControl.redis.get(key))
    try:
        if keyControl(key=key,mac=mac):
            rp = tschat(msg)
            return rp
        elif not keyControl(key=key,mac=mac):
            return {"error":"错误的key"}
    except keyRequests.WrongMac as e:
        return e.message


@app.post("/creatkey")
async def handleCreatKey(request:Request):
    data = await request.json()
    password = data["password"]
    newkey = data["key"]
    if password == config.SUPERUSER_PASSWORLD:
        r=keyControl.creatNewKey(key=newkey)
        if r:
            return "创建成功"
        else:
            return "服务器内部出现问题 创建失败"
    else:
        return "管理员密码不正确"

@app.get("/chat1")
async def money():
    url = 'https://api.openai.com/v1/dashboard/billing/subscription'
    api_key = config.KEY
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"

    }
    subscription_response = requests.get(url, headers=headers)

    # start_date设置为今天日期前99天
    start_date = (datetime.datetime.now() - datetime.timedelta(days=99)).strftime("%Y-%m-%d")
    # end_date设置为今天日期+1
    end_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    billing_url = f"https://api.openai.com/v1/dashboard/billing/usage?start_date={start_date}&end_date={end_date}"

    response1 = requests.get(billing_url, headers=headers)
    return {
        "subscription_response": subscription_response.json(),
        "response1": response1.json()
    }


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host=config.IP, port=config.PORT)