import aiohttp
import asyncio
from aiohttp import web

openai.openai.api_key = "这里填入你的KEY"

async def chat(msg: list) -> dict:
    async with aiohttp.ClientSession() as session:
        url = "https://api.openai.com/v1/engines/gpt-3.5-turbo/completions"
        headers = {"Authorization": f"Bearer {openai.openai.api_key}"}
        data = {
            "prompt": f"{msg}",
            "max_tokens": 60,
            "temperature": 0.5,
            "n": 1,
            "stop": ""
        }
        async with session.post(url, headers=headers, json=data) as resp:
            response = await resp.json()
            return response["choices"][0]["text"]

async def process_dict(request):
    data = await request.json()
    msg = data['msg']
    response = await chat(msg)
    return web.Response(text=response)

app = web.Application()
app.add_routes([web.post('/chat', process_dict)])

if __name__ == '__main__':
    web.run_app(app, port=5701, host="0.0.0.0")
