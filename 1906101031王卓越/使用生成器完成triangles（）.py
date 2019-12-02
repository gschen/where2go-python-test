def triangles(n):
    l=[1]
    for m in range(n):
        print(l)
        l=l[:1]+[l[i]+l[i+1]for i in range(len(l)-1)]+l[-1:]
        return
n=int(input("请输入你要的行数："))
triangles(n)