class Solution:
    def createTargetArray(self, nums, index):
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

            def insert(self, key, value):
                temp = self.head
                i = 0
                while i < key:
                    pre = temp
                    temp = temp.next
                    i = i + 1
                node = Node(value)
                pre.next = node
                node.next = temp
            def app_top(self,val):
                node = Node(val)
                node.next = self.head
                self.head = node

            def print_list(self):
                temp = self.head
                new_list = []
                while temp is not None:
                    new_list.append(temp.data)
                    temp = temp.next
                return new_list

        res = [nums[0]]
        Linked_list = Linked_list()
        Linked_list.initlist(res)
        for i in range(1,len(nums)):
            if index[i] == 0:
                Linked_list.app_top(nums[i])
            else:
                Linked_list.insert(index[i], nums[i])
        return Linked_list.print_list()


solution = Solution()
nums = [1,2,3,4,0]
index = [0,1,2,3,0]

print(solution.createTargetArray(nums,index))
