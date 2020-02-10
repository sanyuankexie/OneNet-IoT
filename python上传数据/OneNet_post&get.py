import requests
import json
import time
import random

api_key='NlkAlp0buwYCSbyc8=A5MnvJIRw='
device_ID='584160273'
headers = {'api-key' : api_key}
url_post = "https://api.heclouds.com/devices/"+device_ID+"/datapoints" #数据点
url_get  = "https://api.heclouds.com/devices/"+device_ID+"/datastreams" # 数据流
def http_post():
    #传输数据,随机数模拟
    Temperature = random.randint(0,100)
    Humidity= random.randint(0,100)
    Carbon= random.randint(0,100)
    Smokescope= random.randint(0,100)
    data = {'datastreams':[
        {"id":"temperature","datapoints":[{"value":Temperature}]},
        {"id":"humidity","datapoints":[{"value":Humidity}]},
        {"id":"carbon","datapoints":[{"value":Carbon}]},
        {"id":"smokescope","datapoints":[{"value":Smokescope}]}
        ]}#id是你的数据流名称
    jdata = json.dumps(data).encode("utf-8")
    r = requests.post(url=url_post, headers=headers, data=jdata)
    print("发送成功：",r.text)
    
def http_get():
    # 获得结果并打印
    r = requests.get(url=url_get, headers=headers)
    print ("返回成功：\n",r.text)
        
if __name__ == "__main__":
    while(True):
        http_post()
        time.sleep(3) #等待三秒
        http_get()
        print ("\n")
