class People(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def raw(self):
        if self.age==10:
            return '辍学回家'
        if self.age==18:
            return '开车去娶媳妇'
        if self.age==22:
            return '上山去砍柴'
s=People('李四',18,'男')
print(s.name,s.age,s.sex,s.raw())
s=People('张三',22,'男')
print(s.name,s.age,s.sex,s.raw())
s=People('王麻子',10,'女')
print(s.name,s.age,s.sex,s.raw())
#王卓越