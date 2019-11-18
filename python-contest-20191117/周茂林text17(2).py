N,M = map(int,input().split())
lis = [x for x in range(N,M+1)]
for i in lis:
    if int(str(i)[0])**2 + int(str(i)[1])**2 > i:
        print(i)
