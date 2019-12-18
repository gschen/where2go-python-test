result = []

def backtrack(nums, track):
    if len(nums) == len(track):
        result.append(list(track))
        return 
    
    for i in nums:
        if i in track:
            continue
            
        track.append(i)
        backtrack(nums, track)
        track.pop()

backtrack([1,2,3,4], [])
print(result)