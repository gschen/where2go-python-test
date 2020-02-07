# lis='123456789'
# print(lis[5:0:-1])
#
# class test:
#     def __init__(self):
#         self.a=123

# class test01:
#     a=123
#     b=456
#     def __init__(self):
#         self.c=123456
# #     def __init__(self,b):
# #         self.c=b
# # n=test01(123) 这个时候b=123
#     def add(self,a,b):
#         c=a+b
#         print(c)
# n=test01()
# print(n.a)
# n.add(1,2)




# class test01:
#     global c
#     c=123
#     def __init__(self,b):
#         self.c=b
#         self.lis=[1,2,3]
#     def add_(self,a,):
#         print(a)
# # 实例化对象.数据属性名
# # 实例化对象.属性名
# n=test01(789)
# m=test01(456)
# n.add_([4,5,6])
# m.add_(1)


# class test01:
#     def __init__(self):
#         self.c01=123
#     def add(self):
#         print(123+456)
# class test02(test01):
#     pass
# n=test02()
# print(n.c01)



class test01:
    def __init__(self):
        pass
    def add(self,a,b):
        print(a+b)
    def dee(self,c,d):
        print(c-d)
n=test01()
n.add(1,3)
n.dee(4,1)