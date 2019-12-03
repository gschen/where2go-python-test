a=input()

# print(a)

b=input()
c=[]
# print(b)

for i in b:
    c.append(i)

for i in c:
    for j in b:
        if i==j:
            s=b.index(i)
            print(s)
