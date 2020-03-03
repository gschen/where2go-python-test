class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def initlist(self, data_list):
        self.head = Node(data_list[0])
        temp = self.head
        for i in data_list[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next

    def is_empty(self):
        if self.head.next == None:
            print("链表为空")
            return True
        else:
            return False

    def get_length(self):
        temp = self.head
        length = 0
        while temp != None:
            length = length + 1
            temp = temp.next
        return length

    def insert(self, key, value):
        if key < 0 or key > self.get_length() - 1:
            print("插入错误")
        temp = self.head
        i = 0
        while i < key:
            pre = temp
            temp = temp.next
            i = i + 1
        node = Node(value)
        pre.next = node
        node.next = temp

    def print_list(self):
        print("linked_list:")
        temp = self.head
        new_list = []
        while temp is not None:
            new_list.append(temp.data)
            temp = temp.next
        print(new_list)


node = Node

data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
linked_list = Linked_list()
linked_list.initlist(data_list)
print('是否为空', linked_list.is_empty())
# print('长度', linked_list.get_length())
# linked_list.insert(2, 100)
# linked_list.print_list()
# print('是否为空', linked_list.is_empty())
# print('长度', linked_list.get_length())
