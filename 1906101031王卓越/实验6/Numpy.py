# #王卓越
# import numpy as np
# c=np.array(np.arange(9).reshape(3,3))
# print(c)
# #可得array函数产生矩阵,reshap将输出的数列排为几行几列输出
class keywords(object):
    def __init__(self,s,name):
        self.name=name
        self.resource=s
    def raw(self):
        if self.name not in self.resource:
            print('该用户未注册')
            name=input('请注册用户名：')
            keyword=int(input('请输入用户名密码:'))
            self.resource[name]=keyword
            return keywords.raw(self)
        if name in self.resource :
            if int(key)==int(self.resource[name]):
                return('登录成功')
            if int(key)!=int(self.resource[name]):
                return('密码错误，请重新尝试')
name=input('输入用户名：')
key=input('输入密码：')
s={}
p=keywords(s)
print(p.raw())
