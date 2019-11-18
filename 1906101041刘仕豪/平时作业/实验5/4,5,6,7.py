'''
4.有一个集合L={'Jack':[90,80,60],'Machile':[80,60,30],'Bob':[80,70,90]},
请使用map分别计算每个同学的
（1）总成绩
（2）平均分
5、使用sorted函数对步骤4的结果总成绩进行
（1）从大到小排序，
（2）从小到大排序
6、使用filter对4题平均成绩不及格的同学过滤
7、使用reduce函数来实现题4中jack同学的总成绩，以及平均分
'''
L={'Jack':[90,80,60],'Machile':[80,60,30],'Bob':[80,70,90]}
#4(1)
all_grades = list(map(sum,[L['Jack'],L['Machile'],L['Bob']]))
print(all_grades)
#4(2)
def a(l):
    k = len(l)
    return sum(l)/k
aver = list(map(a,[L['Jack'],L['Machile'],L['Bob']]))
print(aver)

#5(1)
all_grades.sort()
all_grades.reverse()
print(all_grades)
#5(2)
all_grades.sort()
print(all_grades)

#6
def jige(n):
    return n>=60
pa = filter(jige,aver)
print(list(pa))

#7
from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,L['Jack']))

