from flask import Flask, jsonify, request
import os
app = Flask(__name__)

import openai
#从环境变量中读取OPENAI_API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")
def chat(msg:list):
    rp=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
    )
    return rp




@app.route('/chat', methods=['POST'])
def process_dict():
    data = request.get_json()
    rp=chat(data['msg'])
    return rp

if __name__ == '__main__':
    app.run(port=5701,host="0.0.0.0")
