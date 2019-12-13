def raw(k):
    n=list(str(k))
    if k[0]==k[4] and k[1]==k[3]:
        print("该数是回文数")
    else:
        print("该数不是回文数")
    return k
k=input("请输入一个5位数：")
print(raw(k))
    