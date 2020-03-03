class Node():
    def __init__(self,data):
        self.left=3
        self.right=2
        self.data=data
    def insert(self,Node):
        def raw(left,right):
            if left and right:
                return left,right
        return raw(self.left,self.right)
        # if data<self.data:
        #     if self.left is None:
        #         self.left=data
        #     else:
        #         self.student(data)
        # if data>self.data:
        #     if self.right is None:
        #         self.right=data
        #     else:
        #         self.student(data)
# s=classname(10)
# print(s.student(8))
# print(s.student(6))
s=Node(2)
print(s.insert(Node))