"""
1、	有四个字母：a、b、c、d，能组成多少个互不相同且无重复三位字符串？输出所有结果。
"""

s = {1:"a",2:"b",3:"c",4:"d"}
m = 0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if( a != b ) and (b != c) and (c != a):
                print (s[a],s[b],s[c])
                m += 1
print("能组成%d个互不相同且无重复的三位字符串"%m)