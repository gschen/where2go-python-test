'''
我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。
请你返回由 [low, high] 范围内所有顺次数组成的 有序 列表（从小到大排序）。
示例 1：
输出：low = 100, high = 300
输出：[123,234]
示例 2：
输出：low = 1000, high = 13000
输出：[1234,2345,3456,4567,5678,6789,12345]
'''
def sequentialDigits(low, high):
    b = len(str(high))
    lis = []
    for i in range(1, 10):
        v = str(i)
        for j in range(b):
            if int(v[-1])+1 < 10:
                v += str(int(v[-1])+1)
            else:
                break
            if low <= int(v) <= high:
                lis.append(int(v))
    print(lis)


sequentialDigits(100, 300)
sequentialDigits(1000, 13000)
