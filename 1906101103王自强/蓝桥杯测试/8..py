'''本题目要求你在控制台输出一个由数字组成的等腰三角形'''
x=int(input())
s=''
for i in range(1,3*x):
    s+=str(i)
print('.'*(x-1)+s[0])
x1, n,m= x - 2, 1,4*x-5
while x1>0:
    print('.'*x1+s[n]+'.'*(2*n-1)+s[m])
    x1-=1
    n+=1
    m-=1
print(s[x-1:3*x-2])