#求整数段和
a,b = map(int,input("请输入两个数字：").split())
for m in range(a,b+1):
    print("%d   "%(m),end="")
l=sum(range(a,b+1))
print()