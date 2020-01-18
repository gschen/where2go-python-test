import requests
import json
string = input("请输入想要翻译的：")
url = "https://fanyi.baidu.com/sug"
data = {'kw': string}
res = requests.post(url, data=data)
print(res)
str_json = res.content.decode()  #str
myjson = json.loads(str_json)  #dict
print(myjson['data'][0]['v'])    #位置

