import requests
from lxml import etree
import json


def getPage(page):
    url = f'http://www.zongheng.com/rank/details.html?rt=1&d=1&p={page}'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    }
    req = requests.get(url, headers=header)
    return req.text


def parse(text):
    html = etree.HTML(text)
    names = html.xpath('//div[@class = "rankpage_box"]/div/@bookname')
    auths = html.xpath('//div[@class = "rank_d_book_intro fl"]/div[@class = "rank_d_b_cate"]/@title')
    item = {}
    for name, auth in zip(names, auths):
        item['name'] = name
        item['auth'] = auth
        yield item


def save2File(data):
    with open('C:\\Users\\19145\Desktop\\文件\\爬虫\\data.txt', 'a', encoding='utf-8') as f:
        data = json.dumps(data, ensure_ascii=False) + ',\n'
        f.write(data)


def run():
    for i in range(1, 11):
        text = getPage(i)
        items = parse(text)
        for item in items:
            print(item)
            save2File(item)


if __name__ == '__main__':
    run()
