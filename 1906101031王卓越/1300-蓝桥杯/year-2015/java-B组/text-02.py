# •	观察下面的现象,某个数字的立方，按位累加仍然等于自身。
# 1^3 = 1 
# 8^3  = 512    5+1+2=8
# 17^3 = 4913   4+9+1+3=17
# •	
# 请你计算包括1,8,17在内，符合这个性质的正整数一共有多少个？
nums=0
lis=[]
for num in range(1,100):
    for a in list(str(num**3)):
        lis.append(int(a))
    s=sum(lis)
    if num==s:
        nums+=1
    lis=[]
print(nums)
