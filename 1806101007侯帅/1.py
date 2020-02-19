# class test:
#     def test(self,name):
#
#         return ("hello",name)
#
#
# if __name__ == '__main__':
#
#     t1=test()
#     a=t1.test(input())
#     print(a)
# from itertools import groupby
# lst = sorted([3,2,1,2,3,4,3,4,5,9,10,11])
#
# fun = lambda x: x[1]-x[0]
# for k, g in groupby(enumerate(lst), fun):
#     l1 = [j for i, j in g ]
#     if len(l1) >1:
#         scop = str(l1)
#         print("连续数字范围：{}".format(scop))
import math

lists = sorted([3,3,2,2,1,1])
length = len(lists)
n = 4
for i in range(n):
    one_list = lists[math.floor(i / n * length):math.floor((i + 1) / n * length)]
    print(one_list)
