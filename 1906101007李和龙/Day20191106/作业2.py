"""
实现isPrime()函数，参数为整数，要有参数检测，如
果是质数返回True，否则返回False
"""
def isPrime(x):
    a =list()
    for i in range(2,x-1):
        if x%i==0:
            a.append(i)
    if len(a)==0:
        return "True"
    if len(a) > 0:
        return "False"

m= int(input())
print(isPrime(m))
