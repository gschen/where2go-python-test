class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        head=list(head)
        s=0
        n=len(head)
        for i in range(0,n):
            s+=head[i]*(2**(n-1-i))
        return s

if __name__ =='__main__':
    solution = Solution()
    head=[1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
    print(solution.getDecimalValue(head))
