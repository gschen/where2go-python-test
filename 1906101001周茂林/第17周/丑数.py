'''
请你帮忙设计一个程序，用来找出第 n 个丑数。
丑数是可以被 a 或 b 或 c 整除的 正整数。
示例：
输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
'''
n, a, b, c = map(int, input().split())
lis = list(x for x in range(n * max(a, b, c)))
for x in lis:
    if x % a != 0 or x % b != 0 or x % c != 0:
        lis.remove(x)
print(lis[n - 1])
