class Students(object):
    def __init__(self,name,age,sex,English,math,Chinese):
        self.name = name
        self.age = age
        self.sex = sex
        self.English = English
        self.math = math
        self.Chinese = Chinese
    def zongfen(self):
        print(self.English+self.math+self.Chinese)
    def pingjunfen(self):
        print((self.English+self.math+self.Chinese)/3)
    def xinxi(self):
        print('姓名',self.name)
        print('年龄',self.age)
        print('性别',self.sex)
        print('英语',self.English)
        print('数学',self.math)
        print('语文',self.Chinese)
zhangsan = Students('zhangsan',18,'男',72,84,90)
zhangsan.zongfen()
zhangsan.pingjunfen()
zhangsan.xinxi()