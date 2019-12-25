"""
我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。

请你返回由 [low, high] 范围内所有顺次数组成的 有序 列表（从小到大排序）。



示例 1：

输出：low = 100, high = 300
输出：[123,234]
示例 2：

输出：low = 1000, high = 13000
输出：[1234,2345,3456,4567,5678,6789,12345]

"""
def sequentialDigits(low, high):
    num_list =[]

    for num in range(low,high+1):
        new_num = str(num)
        lenth = len(new_num)
        a = [1] *(lenth-1)
        list1 = [(int(new_num[i]) - int(new_num[i-1])) for i in range(1,lenth)]

        if list1 == a :
            num_list.append(num)
    return num_list

if __name__ == "__main__":
    print(sequentialDigits(1000,13000))
    print(sequentialDigits(100,300))

