import requests

def creatkey(key,password="xxxxxx"):
    data={"password":password,"key":key}
    url = "http://address:2041/creatkey"
    rp=requests.post(url=url,json=data)
    return rp.text

rp=creatkey(key="geluoluo")
print(rp)

