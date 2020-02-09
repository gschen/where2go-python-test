class Solution:
    def palindromePartition(self, s: str, k: int)-> int:
        n = len(s)
        if n%k != 0:#确定分割字符串的步长
            a = int(n/k)+1
        elif n%k == 0:
            a =int(n/k)
        num=0
        for i in range(0,n,a):
            if a!=1:#判断步长是否为1，不为1的时候则需要分割串
                if i+a < n :#当i+a<字符串的长度时，可以直接提取
                    s1 = s[i:i+a]
                else:#当最后的字符个数不满足时，截取最后部分
                    s1 = s[i:]
            elif a==1:
                s1=s[i]
            if len(s1) == 1:
                pass
            elif len(s1) != 1:
                for j in range(len(s1)//2):#回文串判断
                    if s1[j] == s1[-(j+1)]:
                        pass
                    else:
                        num = num + 1
        return  num
if __name__=='__main__':
    solution=Solution()
    s = "tcyhekt"
    k = 2
    print(solution.palindromePartition(s,k))



