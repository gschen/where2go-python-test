
'''
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
'''

# 利用回溯法求解全排列问题 https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-xiang-jie-by-labuladong-2/
result = []

def backtrack(nums, track):
    if len(track) == len(nums):
        # print(track)
        result.append(list(track)) # 为什么此处需要使用list(track)，直接result.append(track)行不行？
        return 
    
    for n in nums:

        if n in track:
            continue
        
        track.append(n)
        backtrack(nums, track)
        track.pop()

backtrack([1,2,3], [])
print(result)