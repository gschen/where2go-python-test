'''
4、标题：测试次数
'''
n=1000
x=1
sums=0
while 1:
    sums += 1
    if n==x:
        print(sums)
        break
    if n>x:
        n=int(n/2)

