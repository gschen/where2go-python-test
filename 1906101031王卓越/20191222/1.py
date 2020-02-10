l=eval(input())
s=[]
for a in l:
    print(a)
    if 10<=a<100 or 1000<=a<10000 or a==100000:
        s.append(a)
print(len(s))
