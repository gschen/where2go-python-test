# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = ''
        while head:
            res += str(head.val)
            head = head.next
        return int(res, 2)
    print(getDecimalValue([1,0,1]))