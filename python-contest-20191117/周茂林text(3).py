N = int(input())
lis = list(map(int,input().split()))
lis2 = [x*x for x in lis]
lis3 = []
for i in range(len(lis2)-3):
    lis3.append(lis2[i] + lis2[i+1] + lis2[i+2])
print(max(lis3))