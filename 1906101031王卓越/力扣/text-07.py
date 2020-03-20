# 101. 对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的。

# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

#     1
#    / \
#   2   2
#    \   \
#    3    3


class Solution(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def add(self,data):
        if self.left:
            self.add(data)
        if self.left is None:
            self.left=data
        if self.right:
            self.add(data)
        if self.right is None:
            self.right=data
    def isSymmetric(self):
        if not self.val:
            return True
        def judge(left,right):
            if left==None and right==None:
                return True
            if left==None or right==None:
                return False
            if left.val!=right.val:
                return False
            return judge(left.left,right.right) and judge(left.right,right.left)
        return judge(self.left,self.right)  
for x in [2,2,3,4,4,3]:
    r=Solution(1)
    print(r.add(x))
# print(r.isSymmetric())
