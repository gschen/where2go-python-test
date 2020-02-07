'''
这里有一个非负整数数组arr，你最开始位于该数组的起始下标start处。当你位于下标i处时，
你可以跳到i + arr[i]或者i - arr[i]。

请你判断自己是否能够跳到对应元素值为0的任意下标处。

注意，不管是什么情况下，你都无法跳到数组之外。
'''
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)
        if not arr or start > n - 1:
            return False
        if arr[start] == 0:
            return True
        Tree = [[start]]
        y = [start]
        i = -1

        while True:
            i += 1
            lis = []
            for j in Tree[i]:
                a = j + arr[j]
                b = j - arr[j]
                if 0 <= a <= n - 1 and a not in y:
                    lis.append(a)
                if 0 <= b <= n - 1 and b not in y:
                    lis.append(b)
            if len(lis) == 0:
                return False
            Tree.append(lis)
            y.extend(lis)
            if 0 in [arr[x] for x in Tree[i + 1]]:
                return True








