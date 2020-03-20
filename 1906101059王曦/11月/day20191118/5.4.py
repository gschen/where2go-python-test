#利用map函数处理列表
def her(l):
    s = 0
    for i in l:
        s = s+i
    return s
def pin(l):
    s = her(l)/3
    return s
L={'Jack':[90,80,60],'Machile':[80,60,30],'Bob':[80,70,90]}

list1 = [L[i] for i in L]
print(list1)
a = list(map(her,list1))
b = list(map(pin,list1))
print(a)
print(b)