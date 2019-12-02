'''
7、	给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''
# def qi():
#     s = str(input("请输入字符串："))
#     A = []
#     for a in range(0, len(s)):
#         if s[a] not in A:
#             A.append(s[a])
#         else:
#             break
#     print(len(A))
#下面借鉴的别人的
def ababab(l):
    l2 = []
    for m in range(len(l)+1):
        for n in range(len(l)+1):
            if m < n and len(l[m:n]) == len(set(l[m:n])):
                l2.append(len(l[m:n]))
    print(max(l2))
