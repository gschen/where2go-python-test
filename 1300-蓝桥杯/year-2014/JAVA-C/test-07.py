count=0
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            for l in range(1,10):
                if i!=j and k!=l and i*k*(j*10+l)==j*l*(i*10+k):
                    count+=1
                    print(i,j,k,l)
print(count)