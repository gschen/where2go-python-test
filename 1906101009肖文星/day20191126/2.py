list=[]
x=abs(int(input()))
for i in range(2,x+1):
    if x%i==0:
        x=x/i
        list.append(i)
        if x%i==0:
            x=x/i
            list.append(i)
a=list
print(a)
#def xwx(n):
#    L=[]
#    while n>1:
#       for i in range(2,n+1):
#            if n % i == 0:
#                n=int(n/1)
#                L.append(i)
#                break
#    return L