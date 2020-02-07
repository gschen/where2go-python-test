# import requests
#
#
# def getPage():
#     url = f'https://nanchong.meituan.com/meishi/pn1/'
#     header = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
#     }
#     req = requests.get(url, headers=header)
#     return req.text
# print(getPage())

import urllib.request
import requests
import csv
import time
from selenium import webdriver
header={'Accept':'application/json',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive','Host':'ta.meituan.com',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }

url='https://nanchong.meituan.com/meishi/'
broswer = webdriver.Chrome()
broswer.get(url)
time.sleep(3)
time.sleep(5)

name=broswer.find_elements_by_xpath('//div[@class = "clear btm"]/div[@class = "info"]/a/h4/text()')
price=broswer.find_elements_by_xpath('//div[@class = "clear btm"]/div[@class = "info"]/a/p[@class = desc]/span/text()')
address=broswer.find_elements_by_xpath('//div[@class = "clear btm"]/div[@class = "info"]/a/p[@class = desc]/text()')
header={'名字','价格','地址'}#表头
with open('C:\\Users\\19145\Desktop\\文件\\爬虫\\dang2.csv', 'a+', newline='', encoding='utf-8')as f:
    writers = csv.writer(f)
    writers.writerow(header)
    for i in range(len(price)):
            listw=[]
            listw = [name[i].text, price[i].text, address[i].text]
            writers.writerow(listw)
