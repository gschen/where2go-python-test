'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def __init__(self):

        self.data = {
                    '2': ['a','b','c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z'],
                }

        self.result = []

    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return list('')
                
        self.backtrack(0, digits, [])

        solution = []

        for line in self.result:
            solution.append(''.join(line))

        return solution

    def backtrack(self, i, nums, track):

        if len(nums) == len(track):
            # print(track)
            self.result.append(list(track))
            return 

        for ch in self.data[str(nums[i])]:

            track.append(ch)
            backtrack(i+1, nums, track)
            track.pop()



