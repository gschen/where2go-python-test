#小朋友崇拜圈
#找规律理解崇拜关系,将一行整数存入数组nums，则崇拜关系可表示为：x崇拜nums[x-1];
#定义变量max保存最长崇拜圈。
#遍历数组进行寻找，找到崇拜的人存入集合中且集合内未有重复元素则计数器加1
#每次遍历后比较计数器con和max，将最大的数保存为max。
#输出max。

N=int(input())
nums=list(map(int,input().split(' ')))#将输入的整数存入列表中
max=0#定义最大人数
for i in range(len(nums)):
    lis = []#用列表模仿崇拜圈
    con=0#定义计数器
    x=nums[i]
    while x not in lis :#判断小朋友是否在圈中，若没在则将他加入圈中并进入循环
        lis.append(x)
        x=nums[x-1]#寻找崇拜者
        con+=1#计数器加一
        if con>max:#比较计数器和最大人数，找到最大的圈
            max=con
print(max)
