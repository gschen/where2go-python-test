k=int(input("请输入一个不大于5位数的整数："))
if k>=10000:
    print("它是5位数")
elif k>=1000 and k<10000:
    print("它是4位数")
elif k>=100 and k<1000:
    print("它是3位数")
elif k>=10 and k<100:
    print("它是2位数")
elif k>=1 and k<10:
