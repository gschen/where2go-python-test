'''
特殊a串数列求和
a,n =map(int,input().split())
i = 0
s = 0
c = 0
while i < n:
    c=a *(10**i)+c
    s = s+c
    i = i+1
print(s)

比较大小
a,b,c=map(int,input().split())
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
print("%d->%d->%d"%(a,b,c))

#华氏摄氏转换表
a,b=input().split()
a,b=eval(a),eval(b)
if(a>b):
    print("Invalid.")
else:
    print("fahr celsius")
    i = a
    while i <= b:
        print("{:d}{:>6.1f}".format(i,5*(i-32)/9))
        i += 2

#求奇数分之一序列前N项和
n = int(input())
s = 0
i = 0
a = 1
b = 1
while i<n:
    c = a/b
    b = b+2
    s = s+c
    i = i+1
print(s)

 #产生每位数字相同的n位数
A,B=map(int,input().split(","))
i = 0
c = 0
while i<B:
    c = A*(10**i) +c
    i = i+1
print(c)
#计算分段函数
x = int(input())
a = 0
b = 1/x
if x == 0:
    print("f(%.1f)=%.1f"%(x,a))
else:
    print("f(%.1f)=%.1f"%(x,b))

#阶梯电价
n =int(input())
if n <=50:
    s = 0.53*n
else:
    s = 0.53*50+(n-50)*(0.53+0.05)
print("cost=%.2f"%s)

#求交错序列前N项和
n = int(input())
a = 1
b = 1
i = 0
s = 0
while i<n:
    c = ((-1)**(i)*a)/b
    a = a+1
    b = b+2
    s = s+c
    i = i+1
print("%.3f"%s)

#转换函数使用
m,n=input().split(",")
n = int(n)
print(int(m,n))

#求平方与倒数序列的部分和
m,n = map(int,input().split())
s = 0
while m<=n:
   s = m*m+1/m+s
   m = m+1
print("sum=%.6f"%s)

#输出三角形面积和周长
import math
a,b,c = map (int,input().split())
if a+b>c and a+c>b and b+c>a:
    s = (a+b+c)/2
    area =math.sqrt(s*(s-a)*(s-b)*(s-c))
    zc = a+b+c
    print("area=%.2f;perimter=%.2f"%(area,zc))
else:
    print("These sides do not correspond to a valid triangle")

# 分段计算居民水费
#为鼓励居民节约用水，自来水公司采取按用水量阶梯式计价的办法，居民应交水费y（元）与月用水量x（吨）相关：
#当x不超过15吨时，y=4x/3；超过后，y=2.5x−17.5
x = int(input())
if x <=15:
    y = (4*x)/3
else:
    y = 2.5*x-17.5
print("%.2f"%y)

#求整数段和
a, b = input().split()
i = int(a)
a = int(a)
b = int(b)
n = 0
x = 0
d = 0
if (a >= -100 and a <= b and b <= 100):
    while (i <= b):
        if (i < 0):
            a = 3
        else:
            a = 4
        if (d == 1):
            print("\n" + a * " " + str(i), end="")
            d = 0
        else:
            print(a * " " + str(i), end="")
        x += i
        i += 1
        n += 1
        if (n == 5):
            d = 1
            n = 0
print("\nSum = {}".format(x))

#大于身高的平均值
n =list(map(int,input().split()))
s = 0
a = len(n)
for i in range(0,a):
    s = s+n[i]
b = s/a
for i in range(0,a):
    if n[i] > b:
        print('{:d}'.format(n[i],end=""))
'''

