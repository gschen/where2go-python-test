import itchat, time
import requests


@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    if not msg['FromUserName'] == Name["a595"]:
        url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg="
        url = url+msg.text
        res = requests.get(url)
        #print(url)
        data = res.json()
        data_content = data['content']
        #print(data_content)
        itchat.send_msg(data_content,msg['FromUserName'])
        itchat.send_msg("自动回复",msg['FromUserName'])
    if msg['Content'] == u'你好':
        itchat.send_msg(msg['User']['RemarkName']+'你好啊',msg['FromUserName'])
        #print(msg['User'])
        #print(msg['User']['RemarkName'])
        #print(msg['FromUserName'])
    print("收到一条消息:", msg.text)
    #print(type(msg.text))


def after_login():


    print("登录成功")


if __name__ == '__main__':
    itchat.auto_login()
    friends = itchat.get_friends(update=True)[0:]
    Name = {}
    Nic = []
    User = []
    for i in range(len(friends)):
        Nic.append(friends[i]["NickName"])
        User.append(friends[i]["UserName"])
    for i in range(len(friends)):
        Name[Nic[i]] = User[i]
    # user_info = itchat.search_friends(name='王永才')
    # print(user_info)
    # if len(user_info) > 0:
    #     # 得到用户名
    #     user_name = user_info[0]['UserName']
    #     print(user_name)
    #     # 发送消息
    #     itchat.send_msg('憨憨', user_name)
    itchat.run()
    # # 获取自己的用户信息，返回自己的属性字典
    # result = itchat.search_friends()
    # print("自己", result)
    # print(result['UserName'])
    # # 根据姓名查找用户
    # result1 = itchat.search_friends(name='王永才')
    # print("王永才：", result1)
    # # 根据微信号查找
    # result2 = itchat.search_friends(wechatAccount='w18982876992')
    # print('w18982876992:', result2)
    # # 查微信号和查姓名可以同时使用
    # result3 = itchat.search_friends(name='王永才', wechatAccount='w18982876992')
    # # 根据USerName查找
    # result4 = itchat.search_friends(userName='@f7dd3cc7c96b301c62e41431752f43377ad4ae8c7b573e3dbb43c723b5d6511a')
    #
    # time.sleep(5)
    # itchat.send("测试", toUserName="filehelper")
    # itchat.run()
