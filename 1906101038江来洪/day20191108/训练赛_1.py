#找出圆内有多少个输入的点
n,a,b,r = map(int,input().split())
s = 0
for i in range(n):
    xi,yi = map(int,input().split())
    if (xi-a)**2+(yi-b)**2<=r**2:
        s += 1
print(s)
