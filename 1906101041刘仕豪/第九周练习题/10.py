'''
10、	有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''
sum =0
for n in range(1,21):
    a,b = 0,1
    t = 0
    while t<n+1:
        a,b = b,a+b
        t+=1
    if n ==1:
        b = 2
    a1,b1 = 0,1
    t1 = 0
    while t1<n:
        a1,b1 = b1,a1+b1
        t1+=1
    if n ==1:
        b1 = 1
    c = b/b1
    sum+=c
print("数列前二十项和为：{}".format(sum))

