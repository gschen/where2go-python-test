'''
给出数字 N，返回由若干 "0" 和 "1"组成的字符串，该字符串为 N 的负二进制（base -2）表示。
除非字符串就是 "0"，否则返回的字符串中不能含有前导零。

示例 1：
输入：2
输出："110"
解释：(-2) ^ 2 + (-2) ^ 1 = 2
'''
class Solution(object):
    def baseNeg2(self, N):

        import math
        str1 = ""
        while(N!=0):
            str1 = str(N%2)+str1
            N = math.ceil(N / -2)
        return str1

print(Solution().baseNeg2(5))