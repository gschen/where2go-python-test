# t1,t2,t3,t4,t5,t6=3,10,6,2,1,7
# T=t1+t2+t3+t4+t5+t6
# averge=T/2
# li=[t1,t2,t3,t4,t5,t6]
# for a in li:

# k=list(''.join(str(eval(s))))
# k=list(''.join(s))
# for x in k:
#     print('{}'.format(x),end='')
# for x in s:
#     print(x)
# class Node():
#     def __init__(self,data):
#         self.left=3
#         self.right=2
#         self.data=data
#     def insert(self,x):
#         for i in range(5):
#             s=self.insert(2)
#         for k in range(5):
#             j=self.insert(1)
#         return s,j  
# p=Node(2)
# print(p.insert(1))
#实例方法 self 
class Node(object):
    def __init__(self,item):
        self.elem=item
        self.left=None
        self.right=None
class Tree(object):
    def __init__(self):#root是定义的根节点
        self.root=None

    def add(self,item):
        node=Node(item)#Tree继承Node类的属性
        if self.root is None:
            self.root=node
            return
        queue=[self.root]#向将节点放入队列中
        while queue:
            cur_node=queue.pop(0)#向队列queue中取出第一个节点进行判断
            if cur_node.left is None:
                cur_node.left=node
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right=node
                return
            else:
                queue.append(cur_node.right)
#广度遍历：
    def breadth_travel(self):
        if self.root is None:
            return
        queue=[self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem,end=' ')#打印出cur_node的值 elem可以输出迭代的值
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)
#三种深度遍历：

#先序遍历：根==》左==》右 的遍历顺序：
    def preorder(self,node):
        if node is None:
            print(node,end=' ')
            return 
        print(node.elem,end=' ')
        self.preorder(node.left)
        self.preorder(node.right)
#中序遍历：左==》根==》右 的遍历顺序：
    # def inorder(self,node):
    #     if node is None:
    #         return

#后序遍历：左==》右==》根 的遍历顺序

if __name__ == "__main__":
    tree=Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)   
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.breadth_travel()
    print(' ')
    print(tree.preorder(tree.root))
    print(' ')
    # print(Node.__dict__)#打印属性
