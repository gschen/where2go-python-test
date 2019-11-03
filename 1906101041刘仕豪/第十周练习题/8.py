'''
8、	给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
'''
def ba(s):
    dic = {}
    for i in range(len(s)):
        for j in range(len(s)):
            if s[j:i:-1] == s[i:j:]:
                dic[i] = j - i
    k = list(dic.keys())[list(dic.values()).index(max(dic.values()))]
    v = max(dic.values())
    print(s[k:v + k + 1:])
