n=int(input())
lis = list(map(int, input().split()))

for i in range(len(lis)-1):
	minindex=i
	for j in range(i+1,len(lis)):
		if lis[j]<lis[minindex]:
			minindex=j
	if minindex!=i:
		lis[i],lis[minindex]=lis[minindex],lis[i]
print(lis)