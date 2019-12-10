class person(object):
    def __init__(self,hight,weight,age,handsome):
        self.hight = hight
        self.weight = weight
        self.age = age
        self.handsme = handsome
    def paoniu(self):
        print('你拥有泡妞的技能')
    def eat(self):
        print('you can eat')

zhangsan = person(170,50,29,86)
lisi = person(180,50,24,97)
zhangsan.paoniu()
lisi.eat()