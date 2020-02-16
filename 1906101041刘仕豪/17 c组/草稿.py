'''
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
import copy
M = 1e4+1
edge = [[M for i in range(n)] for j in range(n)]
print(edge)
for e in edges:
    edge[e[0]][e[1]] = edge[e[1]][e[0]] = e[2]
for i in range(n):
    edge[i][i] = 0
A = copy.deepcopy(edge)
path = [[0 for i in range(n)] for j in range(n)]
print(A)
print(path)
'''


# def permutations(arr, position, end):
#     if position == end:
#         print(arr)
#
#     else:
#         for index in range(position, end):
#             arr[index], arr[position] = arr[position], arr[index]
#             permutations(arr, position + 1, end)
#             arr[index], arr[position] = arr[position], arr[index]
#
#
# arr = [1,2,3,4,5,6,7,8,9]
# print(permutations(arr, 0, len(arr)))
# l = [1,2,3]
# def perm(l):
#     if(len(l)<=1):
#         return [l]
#     r=[]
#     for i in range(len(l)):
#         s=l[:i]+l[i+1:]
#         p=perm(s)
#         for x in p:
#             r.append(l[i:i+1]+x)
#     return r
# print(perm(l))

import math
a = math.pi**math.e
b = math.e**math.pi
print('')