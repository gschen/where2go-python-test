class Solution:
    def palindromePartition(self, s: str, k: int)-> int:
        n = len(s)
        if n%k != 0:
            a = int(n/k)+1
        elif n%k == 0:
            a =int(n/k)
        num=0
        for i in range(0,n,a):
            if a!=1:
                if i+a < n-1 :
                    s1 = s[i:i+a]
                else:
                    s1 = s[i:-1]
            elif a==1:
                s1=s[i]
            if len(s1) == 1:
                num = 0
            elif len(s1) != 1:
                for j in range(len(s1) - 1):
                    if s1[j] == s1[j + 1]:
                        num = 0
                    else:
                        num = num + 1
        return  num
if __name__=='__main__':
    solution=Solution()
    s = "tcymekt"
    k = 4
    print(solution.palindromePartition(s,k))



