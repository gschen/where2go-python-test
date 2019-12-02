N=int(input())
a=0
b=0
c=0
d=0
s=0
while N-s>=11:
    s+=11
    a+=1
while N-s<11 and N-s>=5:
    s+=5
    b+=1
while N-s<5 and N-s>=2:
    s+=2
    c+=1
if N-s==1:
    d+=1
nums = [11, 5, 2, 1]
sum=[a,b,c,d]
result = []
for i in range(4):
    for j in range(sum[i]):
        result.append(int(nums[i]))
ss = result[:-1]
print(ss)
