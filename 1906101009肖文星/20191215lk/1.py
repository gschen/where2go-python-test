# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        lis1=[]
        while head:
            lis1.append(head.val)
            head=head.next
        lis2=[]
        for i in lis1:
            lis2.append(str(i))
        l=''.join(lis2)
        return int(l,2)


