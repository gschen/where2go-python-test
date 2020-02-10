a=range(1,50)
b=0
for i in range(48):
    n=a[i]*a[i+1]-(a[i]+a[i+1])
    for ii in range(48):
        m=a[ii]*a[ii+1]-(a[ii]+a[ii+1])
        if n+m==2015-1225:
            print(i+1)
