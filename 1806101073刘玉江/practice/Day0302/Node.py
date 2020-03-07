class Node:
    def __init__(self, data):
        self.data = data
        self.head = None


class linkList():
    def __init__(self):
        self.head = None

    def initList(self, lis):
        self.head = Node(lis[0])
        temp = self.head
        for i in lis[1,:]:
            node = Node(i)
            temp.next = node
            temp = temp.next
        return lis

