'''

给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:

    def __init__(self):

        self.result = []
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        self.backtrack(nums, [])

        return self.result

    def backtrack(self, nums, track):

        if len(track) == len(nums):

            if track not in self.result:
                self.result.append(list(track))
                
            return 

        # 关键点：面临的选择是nums - track， 如[1,2,3,1] - [1,2] = [3,1]
        aa = nums.copy()
        for i in track:
            aa.remove(i)
        
        for i in aa:

            track.append(i)
            self.backtrack(nums, track)
            track.pop()

