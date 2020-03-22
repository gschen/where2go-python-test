'''

给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
初始化 A 和 B 的元素数量分别为 m 和 n。
示例:
输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
'''
def merge(A,B,m,n):
    for i in range(n):
        for j in range(i,m):
            if A[j]<=B[i]:
                continue
            else:
                A[j],B[i] = B[i],A[j]
                B = sorted(B)
    for i in range(n):
        A[m + i] = B[i]
    return A
print(merge([0,0,0,0,0,0,0,0,0], [1,2,4,6,7,8,9,10,11], 0, 9))
