import itchat
import requests
import re

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'none'


@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing', 'Picture'])
def text_reply(msg):
    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == Name["a595"]:
        # 回复给好友
        # url = "http://www.tuling123.com/openapi/api?key=206c15a5daa743bd97684c2b368389c8&info="
        url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg="
        url = url + msg['Text']
        html = getHtmlText(url)
        message = re.findall(r'\"text\"\:\".*?\"', html)
        reply = eval(message[0].split(':')[1])
        return reply


if __name__ == '__main__':
    itchat.auto_login()

    # 获取自己的UserName
    friends = itchat.get_friends(update=True)[0:]
    Name = {}
    Nic = []
    User = []
    for i in range(len(friends)):
        Nic.append(friends[i]["NickName"])
        User.append(friends[i]["UserName"])
    for i in range(len(friends)):
        Name[Nic[i]] = User[i]
    itchat.run()
