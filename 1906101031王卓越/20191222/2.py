
    
# def raw(s,n,nums,k,x):
#     if nums[x]==nums[x+1]:
#         n.append(nums[x])
#         return raw(s,n,nums,k,x+2)
#     s.append(nums[x])
#     x=x+1
#     nums.remove(n)
#     if len(s)==k:
#         m=nums.index(n[0])
#         n=[]
#         return raw(s,n,nums,k,m)

    

#     s.append(nums[x]
#     if nums[x]==nums[x+1]:
#         n.append(nums[x])
#     if len(s)==k:
#         s=[]
# if s==[]:
#     print('True')
# else:
#     print('Flase')
#                             解答
#一部分
# import collections
# nums=eval(input())
# k=int(input())
# nums.sort()
# dic = collections.defaultdict(int)
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

    

        

    