# nums=eval(input())
# k=int(input())
# nums=sorted(nums)
# lenge=nums
# s=[]
# n=0
# p=0 
# while len(nums)>=0 and p==0:
#     if n<len(nums)-1:
#         if nums[n]==nums[n+1]:
#             n+=1
#             continue
#     s.append(nums[n])
#     nums.remove(nums[n])
#     if len(s)==k:
#         n=0
#         for a in range(k-1):
#             if s[a]!=s[a+1]-1:
#                 print('False')
#                 p=1
#                 break 
#         s=[]
#     if len(nums)==1:
#         s.append(nums[0])
#         if len(s)!=k:
#             print('False')
#             break
#         if len(s)==k:
#             for a in range(k-1):
#                 if s[a]!=s[a+1]-1:
#                     print('False')
#                     break
#                     p=1
#                 if s[a]==s[a+1]-1:
#                     p=1
#                     if a==k-2:
#                         print('True')

#一部分
# import collections
# nums=eval(input())
# k=int(input())
# nums.sort()
# dic = collections.defaultdict(str)
# for num in nums: 
#     dic[num] += 1
# print(dic)
# for num in nums:
#     while dic[num] != 0:
#         for i in range(k):
#             if dic[num + i] == 0:#因为字典dict有defaudict属性，所以当字典dict的key没有num这个值是时，就会返回0. 
#                 print('False')
#             dic[num + i] -= 1
# print('True')

# 二部分
# d={}
# for a in range(1,10):
#     if a not in d:
#         d[a]=0
#     d[a]+=1
# print(d)

#由一二部分可得
# import collections
# dic=collections.defaultdict(int)
# for a in range(1,10):
#     dic[a]+=1
# 等价于:
# d={}
# for a in range(1,10):
#     if a not in d:
#         d[a]=0
#     d[a]+=1




dic=dict()
for num in range(10):
    if num not in dic:
        dic[num]=0
    dic[num]+=1
print(dic)
