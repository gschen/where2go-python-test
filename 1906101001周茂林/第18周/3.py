'''
这里有一个非负整数数组 arr，你最开始位于该数组的起始下标 start 处。当你位于下标 i 处时，你可以跳到 i + arr[i] 或者 i - arr[i]。
请你判断自己是否能够跳到对应元素值为 0 的 任意 下标处。
注意，不管是什么情况下，你都无法跳到数组之外。
示例 1：
输入：arr = [4,2,3,0,3,1,2], start = 5
输出：true
解释：
到达值为 0 的下标 3 有以下可能方案：
下标 5 -> 下标 4 -> 下标 1 -> 下标 3
下标 5 -> 下标 6 -> 下标 4 -> 下标 1 -> 下标 3
'''
def canReach(arr, start):
    lis1, lis2 = [start], []
    le, n = len(arr), 0
    for n in range(n*2):
        for i in lis1:
            if 0 <= i + arr[i] < le:
                lis2.append(i + arr[i])
            if 0 <= i - arr[i] < le:
                lis2.append(i - arr[i])
        for j in lis2:
            if arr[j] == 0:
                return True
        else:
            lis1 = lis2
            lis2 = []


print(canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=5))
print(canReach(arr=[3, 0, 2, 1, 2], start=2))
print('________________')
