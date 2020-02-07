x=int(input())
n=''
for i in range(1,3*x):
    n+=str(i)
n=n[:(4*(x-1))]
# print(n)
y=1
while y<=x:
    if y==1:
        print('%s%s'% ('.'*(x-1),n[0]))
        n=n[1:]
    elif y==x:
        print(n)
    else:
        print('%s%s%s%s'% ('.'*(x-y),n[0],'.'*(2*y-3),n[-1]))
        n=n[1:-1]
    y+=1