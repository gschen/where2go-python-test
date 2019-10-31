#比较大小
a,b,c = map(int,input('请输入三个数：').split())
if a>b and b>c:
    print('%d->%d->%d'% (c,b,a))
elif b>a and a>c:
    print('%d->%d->%d'% (c,a,b))
elif c>a and a>b:
    print('%d->%d->%d'% (b,a,c))
elif c>b and b>a:
    print('%d->%d->%d'% (a,b,c))
elif a>c and c>b:
    print('%d->%d->%d'% (b,c,a))
else:
    print('%d->%d->%d'% (a,c,b))