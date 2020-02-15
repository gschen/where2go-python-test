#小朋友崇拜圈
#找规律理解崇拜关系,将一行整数存入数组nums，则崇拜关系可表示为：x崇拜nums[x-1];
#定义变量max保存最长崇拜圈。
#遍历数组进行寻找，找到崇拜的人存入集合中且集合内未有重复元素则计数器加1
#每次遍历后比较计数器con和max，将最大的数保存为max。
#输出max。

m=int(input())
nums=list(map(int,input().split(' ')))
print(m,list(nums))
max=0
for i in range(len(nums)-1):
    lis = []
    con=0
    x=nums[i]
    while x not in lis :
        lis.append(x)
        x=nums[x-1]
        con+=1
        if con>max:
            max=con
        print(lis)
print(max)
