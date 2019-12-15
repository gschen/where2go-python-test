#coding=utf-8

# no.1
'''给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。
请你返回该链表所表示数字的 十进制值 。
输入：head = [1,0,1]
输出：5
解释：二进制数 (101) 转化为十进制数 (5)'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# ListNode=[1,0,1]
# class Solution:
#     def getDecimalValue(self, head:ListNode) -> int:
#         l=[]
#         sum=0
#         while head:
#             if head:
#                 l.append(head.val)
#                 head=head.next
#         for i in range(len(l)-1,-1,-1):
#             if l[i]==1:
#                 sum+=2**(len(l)-i-1)
#         return sum


class Solution(object):
    def getDecimalValue(self, x) -> int:
        y,sum=len(x)-1,0
        for i in x:
            if y>=0:
                sum=sum+i*2**y
                print(i)
                # print(sum)
                # y=y-1
        # print(sum)
m=eval(input())
n=Solution()
n.getDecimalValue(m)



# no.2
'''我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。
请你返回由 [low, high] 范围内所有顺次数组成的 有序 列表（从小到大排序）。
输出：low = 1000, high = 13000
输出：[1234,2345,3456,4567,5678,6789,12345]'''




# no.3
'''给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。
请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。
输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
输出：2
解释：总和小于 4 的正方形的最大边长为 2

输入：mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
输出：3'''


# no.4
'''给你一个 m * n 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。
如果您 最多 可以消除 k 个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1) 的最短路径，并返回通过该路径所需的步数。如果找不到这样的路径，则返回 -1。
输入： 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
输出：6
解释：
不消除任何障碍的最短路径是 10。
消除位置 (3,2) 处的障碍后，最短路径是 6 。该路径是 (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

输入：
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
输出：-1
解释：
我们至少需要消除两个障碍才能找到这样的路径。'''