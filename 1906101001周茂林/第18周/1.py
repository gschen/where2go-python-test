'''
给你一个整数 n，请你返回 任意 一个由 n 个各不相同的 整数 组成的数组，并且这 n 个数相加和为 0
示例 1：
输入：n = 5
输出：[-7,-1,1,3,4]
解释：这些数组也是正确的 [-5,-1,1,2,3]，[-3,-1,2,-2,4]。
示例 2：
输入：n = 3
输出：[-1,0,1]
'''
def sumZero(n):
    lis = []
    if n % 2 == 0:
        for i in range(1, int((n/2)+1)):
            lis.append(i)
            lis.append(-i)
        return lis
    elif n == 3:
        return [-1, 0, 1]
    elif n == 1:
        return [0]
    else:
        lis.append(n)
        lis.append(-int((n-1)/2))
        lis.append(-int((n-1)/2 + 1))
        for i in range(1, int((n-1)/2)):
            lis.append(i)
            lis.append(-i)
        return lis


n = int(input('：：：'))
print(sumZero(n))
