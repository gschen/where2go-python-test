#判断数组是否满足刚好含有连续的k个数的数列
def jiang(nums,k):
    l = sorted(nums)
    if len(l) % k != 0:
        return False
    else:
        lis = []
        for i in range(len(l) // k):
            li = []
            li.append(l[0])
            l.remove(l[0])
            li1 = l.copy()
            print(li1)
            for n in range(len(li1)):
                if li1[n] == li[-1] + 1 and len(li)+1 != k:
                    li.append(li1[n])
                    l.pop(n)
            lis.append(len(li))
        if sum(lis) == len(l):
            return True
        else:
            return False
print(jiang([1,2,3,3,4,4,5,6],4))
















