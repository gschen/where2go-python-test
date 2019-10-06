#导入需要用到的库request库爬取网络数据，json库转换文件格式
import requests
import json

while True:
    string=input("请输入待翻译的内容：")
    #百度翻译的网址
    url="https://fanyi.baidu.com/transapi"
    #构建头部，构建form表单数据发送post请求
    headers={"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36"}

    data={
        "from": "zh",
        "to": "en",
        "query":string,
        "transtype": "realtime",
        "simple_means_flag": "3",
        "sign": "198772.518981",
        "token": "65430217bbbc3c3c3e8eee164650cefd"
    }
    response=requests.post(url=url,data=data,headers=headers)
    html=response.content.decode()
    #得到的html是json文件格式的内容，所以之后用json提取数据
    html=json.loads(html)
    rep=html["data"][0]["dst"]
    print("翻译的结果：",rep)

