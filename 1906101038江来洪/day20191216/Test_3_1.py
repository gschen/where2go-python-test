#选出大于平均数的身高
list = input('请输入你班级的身高：').split()
i = int(len(list))
S = 0
for x in list:
    x = int(x)
    S = S+x
X = S/i
for a in list:
    a = int(a)
    if a>X:
        print(a,end=' ')