L=[1,1,1,2,3,4,4,4]
L.pop(0)
L.pop(1)
L.pop(3)
L.pop(4)
a=len(L)
print(a,L)
a = 2
b = 1
sum = 0
for i in range(20):
    sum = a / b + sum
    a, b = (a + b), a
print(sum)
x=0
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                for e in range(1,10):
                    if a!=b and a!=c and a!=d and a!=e and b!=c and b!=d and b!=e and c!=d and c!=e and d!=e and(a*10+b)*(c*100+d*10+e)==(a*100+d*10+b)*(c*10+e):
                        x+=1
print(x)
x=int(input(""))
a=x//11
b=(x-a*11)//5
c=(x-(a*11+b*5))//2
e=(x-(a*11+b*5+c*2))
print("11\n"*a)
print("5\n"*b)
print("2\n"*c)
print("1\n"*e)
while a>0:
    print('11')
    a-=1
while b > 0:
    print('5')
    b -= 1
while c>0:
    print('2')
    c-=1#c=c-1
while e>0:
    print('1')
    e-=1
