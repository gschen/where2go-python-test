'''
给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数：
子串中不同字母的数目必须小于等于 maxLetters
子串的长度必须大于等于 minSize 且小于等于 maxSize
示例 1：
输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
输出：2
解释：子串 "aab" 在原字符串中出现了 2 次。
它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。
示例 2：
输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
输出：2
解释：子串 "aaa" 在原字符串中出现了 2 次，且它们有重叠部分。
'''
def maxFreq(s, maxLetters, minSize, maxSize):
    n = 0
    for i in range(minSize, maxSize+1):
        lis = []
        for j in range(len(s[:len(s)-i+1])):
            k = s[j:j+i]
            if len(set(k)) <= maxLetters:
                lis.append(k)
        for p in lis:
            m = lis.count(p)
            if m > n:
                n = m
    return n


print(maxFreq("aababcaab", maxLetters = 2, minSize = 3, maxSize = 4))
print(maxFreq(s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3))
print(maxFreq("abcde", 2, 3, 3))
