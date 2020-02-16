class Solution:
    def countNodes(self, root):
        def height(t):
            h = -1
            while t:
                h += 1
                t = t.left
            return h
        h = height(root)
        nodes = 0
        while root:
            if height(root.right) == h - 1:
                nodes += 2 ** h
                root = root.right
            else:
                nodes += 2 ** (h - 1)
                root = root.left
            h -= 1
        return nodes
