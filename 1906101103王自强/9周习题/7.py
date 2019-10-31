h=100
s=0
for i in range(1,11):
    s+=h
    h/=2
    s+=h
    if i==10:
        s-=h
print('总里程为{}米，第10次跳了{}米'.format(s,h))
#7