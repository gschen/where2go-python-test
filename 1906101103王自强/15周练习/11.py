A,B=map(eval,input().split(' '))
l=[]
for i in range(A,B+1):
    l.append(str(i))
n=len(l)
m=0
while m<n:
    if n-m<5:
        print('     '+'     '.join(l[m:]))
    else:
        str=('     '.join(l[m:m+5]))
        print('     '+str)
    m+=5
sum=0
for j in l:
    sum+=eval(j)
print('sum={}'.format(sum))