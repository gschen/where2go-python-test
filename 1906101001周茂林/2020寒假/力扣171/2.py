'''
给你三个正整数 a、b 和 c。
你可以对 a 和 b 的二进制表示进行位翻转操作，返回能够使按位或运算   a OR b == c  成立的最小翻转次数。
「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。
示例 1：
输入：a = 2, b = 6, c = 5
输出：3
解释：翻转后 a = 1 , b = 4 , c = 5 使得 a OR b == c
示例 2：
输入：a = 4, b = 2, c = 7
输出：1
'''
def minFlips(a, b, c):
    a, b, c = bin(a)[2:], bin(b)[2:], bin(c)[2:]
    n = 0
    la, lb, lc = len(a), len(b), len(c)
    le = max(la, lb, lc)
    a, b, c = '0' * (le - la) + a, '0' * (le - lb) + b, '0' * (le - lc) + c
    for i, j, k in zip(a, b, c):
        print(i, j, k)
        if i == '0' and j == '1' and k == '0':
            n += 1
        elif i == '0' and j == '0' and k == '1':
            n += 1
        elif i == '1' and j == '0' and k == '0':
            n += 1
        elif i == '1' and j == '1' and k == '0':
            n += 2
    return n


# print(minFlips(2, 6, 5))
print(minFlips(8, 3, 5))
