#
#
#
#
#
#
#
#
#
# a = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
# b=a
# def l(x,y):
#     b[x][y]=1
#     b[6-x][6-y]=1
# ans=0
# count=0
# def ter(x,y):
#     print("x,y:",x,y)
#     global ans
#     global count
#     count+=1
#
#     if b[x][y] == 0:
#         l(x,y)
#         if x == 0 or x == 6 or y == 0 or y == 6:
#             ans += 1
#             b=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
#             return
#
#         for i in range(7):
#             for j in range(7):
#                 if (i-x)**2 == 0 and j-y == 0 or i-x == 0 and (j-y)**2 == 1:
#                     print("ok")
#                     ter(i,j)
#
#
#
# ter(3,3)
# print(ans)
# print(count)

a=[1,5,3,4,1]
a.remove(2)
print(a)