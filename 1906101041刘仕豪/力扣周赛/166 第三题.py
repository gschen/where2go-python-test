def disan(nums,threshold):
    import math
    t = 1
    while 1:
        su = 0
        for i in nums:
            su += math.ceil(i/t)
        if su > threshold:
            t += 1
        else:
            return t

print(disan([2,3,5,7,11],11))