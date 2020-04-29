def longestPalindrome(s):
    import collections
    dic=collections.Counter(s)
    res = 0
    res1 = 0
    for i in dic:
        if dic[i] % 2 == 0:
            res += dic[i]
        elif dic[i] % 2 == 1 and dic[i] != 1:
            res = res + dic[i]
            res -= 1
            res1 = res1 + 1
        else:
            res1 += 1
    if res1 > 0:
        res1 = 1
    return res+res1

print(longestPalindrome('abccccdd'))