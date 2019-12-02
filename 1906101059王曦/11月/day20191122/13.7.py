#给定一个正整数N将其表示为数字1,2,5,11相加的形式输出
# 要求上述数字出现的总次数最少(每个数字可以重复使用)。
def hao(x,y):
    list1 = []
    while x>0:
        list1.append(y)
        x-=1
    return list1
n = int(input())
a = 0
m = n
while m>=11:
    m = m-11
    a = a+1
b = m
c = 0
while b>=5:
    b = b-5
    c = c+1
d = b
z = 0
while d>=2:
    d = d-2
    z = z+1
y = d
o = 0
while y>=1:
    y = y-1
    o = o+1
list2 = hao(a,'11')+hao(c,'5')+hao(z,'2')+hao(o,'1')
print(n,'=','+'.join(list2))