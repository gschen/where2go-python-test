'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
示例 1:
输入: s = "anagram", t = "nagaram"
输出: true
示例 2:
输入: s = "rat", t = "car"
输出: false
'''
def quicksot(listx):
    if len(listx) <= 1:
        return listx
    mx = listx[0]
    left = [x for x in listx if x < mx]
    middle = [x for x in listx if x == mx]
    right = [x for x in listx if x > mx]
    return quicksot(left) + middle+ quicksot(right)
s='abaa'
t='aabb'
s=[x for x in s]
t=[x for x in t]
# s1 = quicksot(s)
# t1 = quicksot(t)
#print(s1==t1)

print(quicksot([1,2,3,1,2,3,1,2,3,6,78,45,45,67]))
# def fun(s,t):
#     dic={}
#     for i in s:
#         if i in dic:
#             dic[i] = dic[i] + 1
#         else:
#             dic[i] = 1
#     for i in t:
#         if i in dic:
#             dic[i] -= 1
#         else:
#             return False
#     for i in dic:
#         if dic[i] != 0:
#             return False
#     return True
# s='abcdefg'
# t='abcdefg'
# print(fun(s,t))
