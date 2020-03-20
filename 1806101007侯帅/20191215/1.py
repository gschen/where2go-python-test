class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        h=[]
        sum=0
        while head:
            if head:
                h.append(head.val)
                head=head.next
        for i in range(len(h)-1,-1,-1):
            if h[i]==1:
                sum+=2**(len(h)-i-1)
        return sum










