n=(input('请输入一个5位数：'))
l=list(n)
a=int(l[0])
b=int(l[1])
c=int(l[2])
d=int(l[3])
e=int(l[4])
if a==e and a+1==b and b+1==c and b==d:
    print('这是回文数')
else:
    print('这不是回文数')
    #13