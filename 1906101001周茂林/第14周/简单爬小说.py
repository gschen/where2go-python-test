import requests
import re
url = 'http://www.xbiquge.la/0/951/'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
title = re.findall(r'<meta property="og:title" content="(.*?)"/>', html)[0]
# find = open('%s.txt' % title, 'w' , encoding='utf-8')
chapter = re.findall(r'<div id="list">.*?</dl>', html, re.S)[0]
chapter_list = re.findall(r'href=\'(.*?)\' >(.*?)<', chapter)
for i in chapter_list:
    chapter_url, chapter_title = i
    chapter_url = 'http://www.xbiquge.la%s' % chapter_url
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = 'utf-8'
    chapter_html = chapter_response.text
    chapter_content = re.findall(r'<div id="content">.*?<p>', chapter_html, re.S)[0]
    print(chapter_content)
    exit()
 