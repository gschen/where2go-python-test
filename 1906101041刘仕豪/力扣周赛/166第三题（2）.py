

def chu(nums, threshold):
    import math
    for i in range(1, max(nums)):
        m = 0
        for j in nums:
            m += math.ceil(j / i)
        if m <= threshold:
            return i
