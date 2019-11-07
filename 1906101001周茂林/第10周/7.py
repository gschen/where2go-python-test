'''
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
'''
def ababab(l):
    l2 = []
    for m in range(len(l)+1):
        for n in range(len(l)+1):
            if m < n and len(l[m:n]) == len(set(l[m:n])):
                l2.append(len(l[m:n]))
    print(max(l2))

ababab('abcabcbb')