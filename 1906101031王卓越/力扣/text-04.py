# 5. 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：

# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：

# 输入: "cbbd"
# 输出: "bb"
if s == s[::-1]:
    print(s)
res=s[0]
len_s=1
for a in range(len(s)-1):
    for b in range(a,len(s)):
        if s[a:b+1]==s[a:b+1][::-1] and b-a+1>len_s:
            len_s=b-a+1
            res=s[a:b+1]
print(res)
#动态规划解决
size = len(s)
if size < 2:
    print(s)
dp = [[False for _ in range(size)] for _ in range(size)]
max_len = 1
start = 0
for i in range(size):
    dp[i][i] = True
for j in range(1, size):
    for i in range(0, j):
        if s[i] == s[j]:
            if j - i < 3:
                dp[i][j] = True
            else:
                dp[i][j] = dp[i + 1][j - 1]
        else:
            dp[i][j] = False

        if dp[i][j]:
            cur_len = j - i + 1
        if cur_len > max_len:
            max_len = cur_len
            start = i
print(s[start:start + max_len])


