# def raw():
#     print('hello,world')
# if __name__ == "__main__":
#     raw()
#     print('傻逼')
class Person(object):
    count = 0 
    @classmethod
    def how_many(kw):
        return kw.count
    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1
print (Person.how_many())
p1 = Person('Bob')
print (Person.how_many())
  

