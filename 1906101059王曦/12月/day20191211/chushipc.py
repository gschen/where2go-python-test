#初试爬虫
import requests
import re
url = "https://www.xs386.com/12666/"
response = requests.get(url)
response.encoding = "utf-8"
response.encoding = "gbk"
#print(response.text)
html = response.text
zh = re.findall(r'<div id="list">.*?</div>',html,re.S)[0]
#print(zh)
chapter_info_list = re.findall(r'<dd><a href="(.*?)">(.*?)</a></dd>',zh)
#print(chapter_info_list)
#with open('极灵混沌决.text') as f:
#fb = open('极灵混沌决.text','w',encoding='utf-8')
for chapter_info in chapter_info_list:
    chapter_url,chapter_title = chapter_info
    chapter_url = "https://www.xs386.com%s" % chapter_url
    print(chapter_url,chapter_title)
    chapter_reponse = requests.get(chapter_url)
    chapter_reponse.encoding = 'utf-8'
    chapter_reponse.encoding = 'gbk'
    chapter_html = chapter_reponse.text

