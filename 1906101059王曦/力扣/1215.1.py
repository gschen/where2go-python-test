# 给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。
# 请你返回该链表所表示数字的 十进制值 。

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        s = [str(i) for i in l]
        s = ''.join(s)
        return int(s,2)
