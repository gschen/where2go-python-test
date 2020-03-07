# 15. 三数之和
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

 

# 示例：

# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
nums=[-2,0,0,2,2]
res=[]
n=len(nums)
if n<3:#判断nums长度，如果小于3不可能存在=0的三元组，直接返回res=[]
    print(res)
nums=sorted(nums)#建立双指针与对nums采用sorted排序
for a in range(len(nums)-2):
    num1=a+1
    num2=n-1
    if a>=1:
        if nums[a]==nums[a-1]:
            continue
    while num1<num2:#双指针详解：首先定义最小的指针为a，将其视为静态指针，其次双指针分别为num1与num2，满足右边为num2，所以num2>num1，
        sum=nums[a]+nums[num1]+nums[num2]
        if sum>0:
            num2-=1
        if sum<0:
            num1+=1
        if sum==0:
            res.append([nums[a],nums[num1],nums[num2]])
            num1+=1
            num2-=1
            while num1<num2 and nums[num2]==nums[num2+1]:
                num2-=1
            while num1<num2 and nums[num1]==nums[num1-1]:
                num1+=1    
print(res)
#建立双指针与对nums采用sorted排序（从小到大排序）
#判断nums长度，如果小于3不可能存在=0的三元组，直接返回res=[]
#双指针详解：首先定义最小的指针为a，将其视为静态指针，其次双指针分别为num1与num2，满足右边为num2，所以num2>num1，
#设sum=nums[a]+nums[num1]+nums[num2]判断其sum值大于0还是小于0还是=0，如果大于0表示右指针num2过大，所以执行num2-=1

        




                
