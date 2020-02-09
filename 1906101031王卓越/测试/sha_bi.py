class student(object):
    def __init__(self):
        self.name='jack'
        self.age=18
        self.sex='boy' 
        self.English=60
        self.Math=80
        self.Chinese=70
    def mark_(self):
        a=self.English+self.Math+self.Chinese
        b=a/3
        return self.name,self.age,self.sex,'总成绩：%d'%a,'平均成绩：%d'%b
p=student()
print(p.mark_())

# class Person(object):
#     count=0
#     def __init__(self, name):
#         self.name = name
#         Person.count += 1
# p1 = Person('Bob')
# print (Person.count ) # 1
# p2 = Person('Alice')
# print (Person.count)  # 2
# p3 = Person('Tim')
# print (Person.count) # 3

# class Person(object):
#     address = 'zhejiang'
#     def __init__(self, name):
#         self.name = name 
# p1 = Person('Bob')
# p2 = Person('Alice') 
# print ('Person.address = ' + Person.address)  # zhejiang
# p1.address = 'shanxi'
# print ('p1.address = ' + p1.address)  # shanxi
# print ('Person.address = ' + Person.address)  # zhejiang
# print ('p2.address = ' + p2.address) # zhejiang