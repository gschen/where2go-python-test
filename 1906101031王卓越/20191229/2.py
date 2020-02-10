class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left #左子树
        self.right=right #右子树
    def preTraverse(root):
        # '''
        # 前序遍历
        # '''
        if root==None:
        return 
        print(root.value)
        preTraverse(root.left)
        preTraverse(root.right)
        def midTraverse(root):