class ListNode(object):
    def __init__(self, data):
        self.data= data
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        nextNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return nextNode

class Linked_list:
    def __init__(self):
        self.head=None
    def initlist(self,linklist):
        self.head=linklist[0]
        temp = self.head
        for i in linklist[1,:]:
            node=ListNode(i)
            temp.next=node
            temp=temp.next
