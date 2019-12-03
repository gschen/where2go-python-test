# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 10:54:38 2018

@author: administrator
"""
inp=input()
l=len(inp)
#主要用到的就是chr和ord

#chr把ascii转为str
#ord把str转为ascii

for i in range(l):
    if ord('A') <=ord(inp[i])<=ord('Z'):
        onew=ord('A')+((ord(inp[i])-ord('A'))+3)%26
    elif ord('a') <=ord(inp[i])<=ord('z'):
        onew=ord('a')+((ord(inp[i])-ord('a')) + 3 )%26
    else:
        onew=ord(inp[i])#不是字符之外的数，直接转化成ASCII
    new=chr(onew)
    print(new,end='')
# s = input()
# t = ""
# for c in s:
#     if 'a' <= c <= 'z': #str是可以直接比较的
#         t += chr( ord('a') + ((ord(c)-ord('a')) + 3 )%26 )
#     elif 'A'<=c<='Z':
#         t += chr( ord('A') + ((ord(c)-ord('A')) + 3 )%26 )
#     else:
#         t += c
# print(t)
print(chr(64))
