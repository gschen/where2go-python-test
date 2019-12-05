
import math as m
l = list(map(int,input().split()))
zuo = [[l[0],l[1]],[l[2],l[3]],[l[4],l[5]]]
a = m.sqrt((l[0]-l[2])**2+(l[1]-l[3])**2)
b = m.sqrt((l[0]-l[4])**2+(l[1]-l[5])**2)
c = m.sqrt((l[2]-l[4])**2+(l[3]-l[5])**2)
p = (a+b+c)/2
s = m.sqrt(p*(p-a)*(p-b)*(p-c))
if l[0]==l[2] and l[2]==l[4] and l[0]==l[4]:
    print('NT')
elif (l[0]-l[2])/(l[1]-l[3]) == (l[4]-l[2])/(l[5]-l[3]):
    print('NT')
elif a == b or b == c or a == c:
    print('IT %.2f'%s)
else:
    print('T %.2f'%s)