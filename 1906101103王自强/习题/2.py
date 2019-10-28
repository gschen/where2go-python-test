import math
for i in range(1,100000):
    m=int(math.sqrt(100+i))
    n=int(math.sqrt(268+i))
    if m*m==i+100 and n*n==i+268:
        print(i)
#20