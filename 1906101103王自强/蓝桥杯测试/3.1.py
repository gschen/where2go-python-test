#   0123456789
l=['LANQIAOOXX'#0
   'ZOEXCCGBDK'#10
   'MOOYWKHIOO'#20
   'BCCAPLJQOO'#30
   'SLANIIAOOO'#40
   'RSLAQQIAOI'#50
   'XINZVNALOO'#60
   'CAAIQNALOO'#70
   'LANQIAOLOO'#80
   'OOOOBOOOPO']#90
sum=0
#水平
n=10
for y in range(0,n*n,n):
    for x in range(0,n-6):
        x=x+y
        a=l[0][x:x+7]
        a1=a[::-1]
        if a=='LANQIAO'or a1=='LANQIAO':
            sum+=1
#竖直
for y in range(0, (n - 6) * n, n):
    for x in range(n):
        x=x+y
        b=l[0][x]+l[0][x+n]+l[0][x+n*2]+l[0][x+n*3]+l[0][x+n*4]+l[0][x+n*5]+l[0][x+n*6]
        b1=b[::-1]
        if b == 'LANQIAO' or b1 == 'LANQIAO':
            sum += 1
#右斜
for y in range(0,(n-6)*n,n):
    for x in range(n-6):
        x=x+y
        c=l[0][x]+l[0][x+1+n]+l[0][x+2+n*2]+l[0][x+3+3*n]+l[0][x+4+4*n]+l[0][x+5+5*n]+l[0][x+6+6*n]
        c1=c[::-1]
        print(c,c1)
        if c == 'LANQIAO' or c1 == 'LANQIAO':
            sum += 1
#左斜
for y in range(0,(n-6),n):
    for x in range(6,n):
        x=x+y
        d = l[0][x] + l[0][x - 1 + n] + l[0][x - 2 + 2*n] + l[0][x - 3 + 3*n] + l[0][x - 4 + 4*n] + l[0][x - 5 + 5*n] +l[0][x - 6 + 6*n]
        d1=d[::-1]
        print(d,d1)
        if d == 'LANQIAO' or d1 == 'LANQIAO':
            sum += 1
print(sum)