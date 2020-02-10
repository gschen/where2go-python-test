# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
[3,9,20,null,null,15,7]
'''

n3, n9, n20, n15, n7 = [TreeNode(i) for i in [3, 9, 20, 15, 7]]
n3.left, n3.right = n9, n20
n20.left, n20.right = n7
