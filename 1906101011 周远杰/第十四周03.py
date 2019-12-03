#有一分数序列:2/1,3/2,5/3,8/5,13/8,21/13 求出这个数列的前20项之和
#示：用递归


def zhou1(n):
    i,a,b=0,2,1
    if n==1:
        return a/b
    else:
        if i<n:
            b,a=a,a+b
            i=i+1
            return a/b
def zhou2(n):
    a,b=2,1
    if n==1:
        return a/b
    else:
        return zhou1(n)+zhou2(n-1)
n=int(input('输入需加到的项数:'))
print(zhou2(n))