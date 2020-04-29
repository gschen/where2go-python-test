l,v1,v2,t,s=input()
time=l/v1
i=1
while i<time :
    if i==1:
        s1=v1*i
        s2=v2*i
    if s1-s2>=t:
        s1=s1
        s2=s2+v2*s
        i=i+s
    else:
        s1=(i-s)*v1
        s2=i*v2
        i=i+1

