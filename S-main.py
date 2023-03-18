from fastapi import FastAPI
from pydantic import BaseModel
import openai

url = 'https://api.openai.com/v1/chat/completions'
openai.api_key = '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'



app = FastAPI()

def chat(ID:str,msg:list):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user", "content": msg
        }]
    )
    a = response['choices'][0]['message']['content']
    return a



class Form(BaseModel):
    ID: str
    msg: list

@app.post("/chat")
async def _(form: Form):
    if form == "":
        pass
    else:
        rp = chat(form.msg)

    return rp




@app.get("/")
async def hello_world():
    return {"message": "你好"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5700)