n=1
s=2
while True:
    x=[]
    s+=1
    for i in range(2,s):
        x.append(s%i)
    if 0 not in x:
        n+=1
    if n==2019:
        break
print(s)
