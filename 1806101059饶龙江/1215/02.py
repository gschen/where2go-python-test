class Solution:
    def sequentialDigits(self, low: int, high: int):
        lis1=[]
        for i in range(low,high+1):
            s=str(i)
            n=0
            for j in range(len(s)-1):
                if eval(s[j])+1==eval(s[j+1]):
                    n+=1
            if n==len(s)-1:
                lis1.append(i)
        return lis1

if __name__ =='__main__':
    solution = Solution()

    low=1000
    high=13000
    print(solution.sequentialDigits(low,high))






