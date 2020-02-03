'''
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

示例:
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

输入: S = "3z4"
输出: ["3z4", "3Z4"]

输入: S = "12345"
输出: ["12345"]
注意：

S 的长度不超过12。
S 仅由数字和字母组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-case-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import *

# class Solution:
#     def letterCasePermutation(self, S: str) -> List[str]:

            
# 大小写字符转换
def upper_lower_change(ch):
    if ord(ch) < 97:
        return chr(32 + ord(ch))
    else:
        return chr(ord(ch) - 32)

result = []

numbers = [str(i) for i in range(10)]

def backtrack(i, S):
    if i == len(S):
        print(S)
        result.append(list(S))
        return 
    

    if S[i] in numbers:
        backtrack(i+1, S)
    else:
        
        # 做出选择
        S[i] = upper_lower_change(S[i])
        backtrack(i+1, S)
        
        # 还原选择
        S[i] = upper_lower_change(S[i])
        backtrack(i+1, S)


backtrack(0, list('a1b2'))

