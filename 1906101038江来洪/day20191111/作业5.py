#用生成器打出杨辉三角
def triangles(n):
    L = [1]
    for m in range(n):
        yield L
        L = L[:1] + [L[i]+L[i+1] for i in range(len(L)-1)] + L[-1:]
n = int(input('请输入你要的行数：'))
l = triangles(n)
for i in l:
    print(i)