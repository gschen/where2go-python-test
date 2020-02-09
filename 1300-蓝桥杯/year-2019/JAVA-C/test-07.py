n=3
m=4
a=[1,3,5,7,9,8,7,6,3,5,9,7]
b=[]
d=[]
for i in range(0,len(a),m):
    for iii in range(m):#0123
        c=[]
        for ii in range(1,len(b)+1):#123
            c.append(b[-ii][iii])
    d.append(c)
print(d)
