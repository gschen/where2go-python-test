#找出给定字符串中无重复字符的最长子串
def wcfzc(str1):
    list = []
    for m in range(len(str1)+1):
        for n in range(len(str1)+1):
            if m < n and len(str1[m:n]) == len(set(str1[m:n])):
                list.append(len(str1[m:n]))
    return max(list)
str1 = input('请输入字符串：')
print(wcfzc(str1))