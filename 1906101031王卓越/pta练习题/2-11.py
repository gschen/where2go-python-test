m,n=map(int,input().split())
def raw(m,n,sum,sums):
    if m<n+1:
        sums=sums+1/m
        sum=sum+m**2
        return raw(m+1,n,sum,sums)
    if m==n+1:
        return '%.6f' % float(sum+sums)
print(raw(m,n,0,0))