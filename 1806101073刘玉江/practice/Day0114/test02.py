import requests
from lxml import etree
import json


def getPage(page):
    url = f'https://nanchong.meituan.com/meishi/pn{page}/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    }
    req = requests.get(url, headers=header)
    return req.text


def parse(text):
    html = etree.HTML(text)
    names = html.xpath('//div[@class = "clear btm"]/div[@class = "info"]/a/h4/text()')
    addresss = html.xpath('//div[@class = "clear btm"]/div[@class = "info"]/a/p[@class = desc]/text()')
    moneys = html.xpath('//div[@class = "clear btm"]/div[@class = "info"]/a/p[@class = desc]/span/text()')
    item = {}
    for name, address,money in zip(names, addresss,moneys):
        item['name'] = name
        item['address'] = address
        item['money'] = money
        print(item)
        yield item


def save2File(data):
    with open('C:\\Users\\19145\Desktop\\文件\\爬虫\\ncfood.txt', 'a', encoding='utf-8') as f:
        data = json.dumps(data, ensure_ascii=False) + ',\n'
        f.write(data)


def run():
    for i in range(1, 77):
        text = getPage(i)
        items = parse(text)
        for item in items:
            print(item)
            save2File(item)


if __name__ == '__main__':
    run()
