# def add(self, item):
#     """
#     广度优先遍历方式添加结点
#     :param item:
#     :return:
#     """
#     if self.root is None:
#         self.root = Node(item)
#     else:
#         queue = []
#         queue.append(self.root)

#         while len(queue) > 0:
#             node = queue.pop(0)
#             if not node.lchild:
#                 node.lchild = Node(item)
#                 return
#             else:
#                 queue.append(node.lchild)
#             if not node.rchild:
#                 node.rchild = Node(item)
#                 return
#             else:
#                 queue.append(node.rchild)

# def breadh_travel(self):
#     """广度优先遍历"""
#     if self.root is None:
#         return
#     queue = []
#     queue.append(self.root)
#     while len(queue)>0:
#         node = queue.pop(0)
#         print(node.item, end=" ")
#         if node.lchild:
#             queue.append(node.lchild)
#         if node.rchild:
#             queue.append(node.rchild)
class classname(object):
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def student(self,data):
        if data<self.data:
            if self.left is None:
                self.left=data
            else:
                self.student(data)
        if data>self.data:
            if self.right is None:
                self.right=data
            else:
                self.right.student(data)
s=classname(10)
print(s.student(8))



