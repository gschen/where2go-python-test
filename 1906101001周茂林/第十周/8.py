'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
'''
def ssss(l):
    d = {}
    for m in range(len(l)+1):
        for n in range(len(l)+1):
            if m < n and l[m:n][::-1] == l[m:n]:
                d.update({l[m:n]:len(l[m:n])})
    aa = max(d.values())
    for key,values in d.items():
        if values == aa:
            print(key)


ssss('babad')