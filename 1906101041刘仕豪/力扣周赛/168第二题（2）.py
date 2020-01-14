def isPossibleDivide(nums, k):
    n = len(nums)
    if n % k != 0:
        return False
    # 用集合记录可能的数字
    s = set(nums)
    minList = list(s)
    minList.sort()
    # 用字典存储每个数字出现的次数
    d = dict()
    for num in nums:
        if num not in d:
            d[num] = 0
        d[num] += 1
    # 判断每组是否可由k个连续数字构成
    m = n // k  # m组
    start = 0  # 起始位置
    for mi in range(m):
        if start >= len(minList):
            return False
        minv = minList[start]
        flag = True
        t = start
        for key in range(minv, minv + k):
            if key not in d:
                return False
            if d[key] < 1:
                return False
            elif d[key] == 1:
                d[key] -= 1
                t += 1
            elif d[key] > 1:
                d[key] -= 1
                if flag:
                    start = t
                    flag = False
        if flag:
            start = t
    return True

