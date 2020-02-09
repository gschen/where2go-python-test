#分析知道，这个数字是个两位数,且超过30
for i in range(31,100):
    a= i**2
    b=i**3
    s=str(str(a)+str(b))
    t=set(s)
    if len(t)==10:
        print(i)
