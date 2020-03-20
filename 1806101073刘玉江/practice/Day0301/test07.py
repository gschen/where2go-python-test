'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
'''
def climbStairs(n):
    ls=[]
    for i in range(n):
        if i == 0:
            ls.append(1)
        elif i == 1:
            ls.append(2)
        else:
            ls.append(ls[i-2]+ls[i-1])
    return ls[-1]
print(climbStairs(100))