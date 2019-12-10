'''
给定一个数组，你需要删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度和新的数组
输入样例：[1,1,1,2,3,4,4,4]
输出样式：4 [1,2,3,4]
'''

lis = list(set(eval(input())))
print(len(lis), lis)

# lis = eval(input())
# for i in lis:
#     if lis.count(i) >= 2:
#         lis.remove(i)
# print(len(lis), lis)
