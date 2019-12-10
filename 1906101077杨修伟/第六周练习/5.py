n =int(input())
for i in range(1,n+1):
    for j in range (1,i+1):
        print("%dx%d=%-2d"%(j,i,j*i),end='\t')
    print()