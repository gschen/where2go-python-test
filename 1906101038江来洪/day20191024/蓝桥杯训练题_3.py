#比较大小
a,b,c = map(int,input('请输入三个数：').split())
if a>b and b>c:
    print(c,b,a)
elif b>a and a>c:
    print(c,a,b)
elif c>a and a>b:
    print(b,a,c)
elif c>b and b>a:
    print(a,b,c)
elif a>c and c>b:
    print(b,c,a)
else:
    print(a,c,b)