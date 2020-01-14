def raw(a,b,N,sum,k):
    if k<N-1:
        if k%2==0:
            sum=sum-a/b
            return raw(a+1,b+2,N,sum,k+1)
        if k%2!=0:
            sum=sum+a/b
            return raw(a+1,b+2,N,sum,k+1)
    if k==N-1:
        return '%.3f'% sum
N=int(input())
print(raw(2,3,N,1,0))