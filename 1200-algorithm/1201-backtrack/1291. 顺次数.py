'''


我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。

请你返回由 [low, high] 范围内所有顺次数组成的 有序 列表（从小到大排序）。

 

示例 1：

输出：low = 100, high = 300
输出：[123,234]
示例 2：

输出：low = 1000, high = 13000
输出：[1234,2345,3456,4567,5678,6789,12345]
 

提示：

10 <= low <= high <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sequential-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
result = []

def backtrack(low, high, track):

    num = 0
    for i in track:
        num = 10 * num + i

    if num >= low and num <= high:

        if num not in result:

            print(num)
            result.append(num)

        return 
    
    max = track[-1]

    for i in range(max+1, 10):
        if i != track[-1] +1 :
            continue

        track.append(i)
        backtrack(low, high, track)

        if num <= high:
            continue
        else:
            track = [track[0]+1]
            backtrack(low, high, track)
         

backtrack(1000, 13000, [1])
