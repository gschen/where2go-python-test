'''
给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。
示例 ：
输入：n = 234
输出：15
解释：
各位数之积 = 2 * 3 * 4 = 24
各位数之和 = 2 + 3 + 4 = 9
结果 = 24 - 9 = 15
'''
def subtractProductAndSum(n):
    a, b = 1, 0
    for i in str(n):
        a *= int(i)
        b += int(i)
    return a-b

print(subtractProductAndSum(234))
