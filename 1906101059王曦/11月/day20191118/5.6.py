#利用reduce求和
from functools import reduce
def add(x,y):
    return x+y
L={'Jack':[90,80,60],'Machile':[80,60,30],'Bob':[80,70,90]}
list1 = [L[i] for i in L]
list2 = [reduce(add,i) for i in list1]
print(list2)
