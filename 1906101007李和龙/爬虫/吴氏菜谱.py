import requests
from bs4 import BeautifulSoup

food = requests.get("http://www.xiachufang.com/explore/")
html = food.text
bss = BeautifulSoup(html,'html.parser')
def food_name():
    item = bss.find_all("div",class_="info pure-u")
    for  item in item:
        print(item.find("a").text)

def food_material():
    item = bss.find_all("p", class_="ing ellipsis")
    for item in item:
        print(item.find("span").text)
food_name()
