lower,upper=map(int,input().split())
n=lower
if lower>upper:
    print('Invalid.')
else:
    print('fahe celsius')
    while n<=upper:
        k=5*(n-32)/9
        print('{}{:>6.1f}'.format(n,k))
        n=n+2


