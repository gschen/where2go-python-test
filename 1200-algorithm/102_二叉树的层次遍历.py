# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

from typing import *
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        result = []
        if root == None:
            return result

        queue = []
        queue.append(root)

        while len(queue) != 0:
            level_len = len(queue)

            level_all = []

            for i in range(level_len):
                node = queue.pop(0)
                level_all.append(node.val)

                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)

            result.append(level_all)

        return result


class Test(unittest.TestCase):

    def test_01(self):

        n3, n9, n20, n15, n7 = [TreeNode(i) for i in [3, 9, 20, 15, 7]]
        n3.left, n3.right = n9, n20
        n20.left, n20.right = n15, n7

        self.assertEqual(Solution().levelOrderBottom(n3), [
            [3],
            [9, 20],
            [15, 7]
        ])


if __name__ == '__main__':
    unittest.main()
