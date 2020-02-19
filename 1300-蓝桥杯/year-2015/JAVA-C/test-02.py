# coding=utf-8

'''
第二题：立方尾不变
题目描述
有些数字的立方的末尾正好是该数字本身。
比如：1,4,5,6,9,24,25,....

请你计算一下，在10000以内的数字中（指该数字，并非它立方后的数值），符合这个特征的正整数一共有多少个。

请提交该整数，不要填写任何多余的内容。

'''
sum_nuber = 0
for i in range(1,26):
    n=str(i**3)
    s=str(i)
    l=len(s)
    if eval(n[-l:])==i and eval(n[-l])!=0:
        sum_nuber+=1
print(sum_nuber)


'''第二种方法'''
# (思路：直接根据条件，用%求余拿到它的尾数对照就可以了)
# n=0
# for i in range(1,100):
#     if i==(i**3%(10**(len(''.join('%d'% i))))):
#         n+=1
#         # print(i)
# print(n)