import openai
import config
import json
openai.api_key=config.KEY


def chat(msg:list[dict[str,str]]) -> dict:
    """

    :param msg: a history message list
    :return: a python object
    """
    rp=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
    )

    return rp

def tschat(msg:list[str]) -> str:
    return "ts"

