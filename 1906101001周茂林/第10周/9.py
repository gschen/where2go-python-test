'''
给定一个包含 n 个整数的数组 nums.
判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
'''
def numsabc(nums):
    s = []
    for a in nums:
        for b in nums:
            for c in nums:
                if a <= b <= c and a+b+c == 0:
                    s.extend(sorted([[a,b,c]]))
    z = []
    for i in s:
        if i not in z:
            z.append(i)
    n = 0
    for o in nums:
        if o == 0:
            n += 1
    if [0,0,0] in z and n < 3:
        z.remove([0,0,0])
    for p in z:
        print(''.join(str(p)))


numsabc([-1,0,1,2,-1,-4])