from aiohttp import web

import json

import config
from getChat import chat,tschat
from keyRequests import isPass

app=web.Application()
routes = web.RouteTableDef()


async def handleChat(request:web.Request):
    data = await request.json()
    msg = data["msg"]
    key = data["key"]



    if not isPass(key=key):
        return web.Response(text="错误的key")
    #print(msg[0])

    rp = tschat(msg) #测试用tschat 部署用chat
    return web.Response(text=str(rp))




app.router.add_post("/chat2",handleChat)


if __name__ == "__main__":

    print("========      ChatRetransmission-ACS    ========")
    web.run_app(app,port=config.PORT,host=config.IP)