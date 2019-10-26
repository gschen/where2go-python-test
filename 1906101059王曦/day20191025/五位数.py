s = eval(input('请输入一个小于或等于五位的数：'))
if s/10000>1:
    print(5)
    a = s//10000
    b = (s//1000)-a*10
    c = (s//100)-a*100-b*10
    d = (s//10)-a*1000-b*100-c*10
    e = s-a*10000-b*1000-c*100-d*10
    print(e,d,c,b,a)
elif s/1000>1:
    print(4)
    a = (s // 1000)
    b = (s // 100)-a * 10
    c = (s // 10)-a * 100-b * 10
    d = s-a * 1000 - b * 100 - c * 10
    print( d, c, b, a)
elif s/100>1:
    print(3)
    a = s // 100
    b = (s//10)-a*10
    c = s-a*100-b*10
    print(c, b, a)
elif s/10>1:
    print(2)
    a= s//10
    b= s-a*10
    print(b, a)
else:
    print(1)
    print(1)