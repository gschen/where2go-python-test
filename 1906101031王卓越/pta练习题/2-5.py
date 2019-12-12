def raw(k,N,sum,x):
    if x<N:
        sum=sum+1/k
        return raw(k+2,N,sum,x+1)
    if x==N:
        return 'sum=',sum
N=int(input())
print(raw(1,N,0,0))
