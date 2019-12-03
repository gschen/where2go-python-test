x=int(input(""))
a=x//11
b=(x-a*11)//5
c=(x-(a*11+b*5))//2
e=(x-(a*11+b*5+c*2))
while a>0:
    print('11')
    a-=1
while b > 0:
    print('5')
    b -= 1
while c>0:
    print('2')
    c-=1
while e>0:
    print('1')
    e-=1

