class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> ist[int]:
        from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        L = []
        def PreOrder(root):
            if root == None:
                return
            L.append(root.val)
            PreOrder(root.left)
            PreOrder(root.right)
        PreOrder(root1)
        PreOrder(root2)
        return list(sorted(L))