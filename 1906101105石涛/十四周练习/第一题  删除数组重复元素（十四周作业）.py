# coding=utf-8
'''
1给定一个数组，你需要删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度和新的数组
输入样例：[1,1,1,2,3,4,4,4]
输出样式：4        [1,2,3,4]
'''
L=[]
l=set([1,1,1,2,3,4,4,4])
# print(l)
for i in l:
    # print(i)
    L.append(i)
print('列表的元素个数为:',len(L),'列表为:',L)
print('列表的元素个数为:',len(L),'列表为:',list(l))

