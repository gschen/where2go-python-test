N = int(input())
nums = []
result1 = []
result2 = []
for i in range(N):
    num = list(map(int,input().split()))
    nums += num
nums = sorted(nums)
minnum,maxnum = min(nums),max(nums)
for n in range(minnum,maxnum+1):
    if nums.count(n) == 0:
        result1.append(n)
    elif nums.count(n) == 2:
        result2.append(n)
print(result1[0],result2[0])