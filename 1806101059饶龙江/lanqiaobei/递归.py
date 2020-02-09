def shulie(n):
    if n<=1:
        return n
    else:
        return shulie(n-1)+shulie(n-2)
#for i in range(0,10):
 #   print(shulie(i),end=',')



def shuchu(n):
    if n<10:
        return n
    else:
        return str(n%10)+str(shuchu(n//10))

#print(shuchu(12345))
#n=int(input('请输入层数'))
def ta(n,A,B,C):
    if n==1:
        print(A,'--->>',C)
    else:
        ta(n-1,A,C,B) #中间过程，移动盘片
        print(A,'--->>',C)
        ta(n-1,B,A,C)#s当n减少1时，将A作为缓冲柱

#print(ta(n,'A','B','C'))
str1=input('请输入字符串:')

def pailie(str1):
    lis=[]
    n=len(str1)
    if n==1:
        return str1
    else:
        for i in range(n):
            a=str1[i]
            new_s=str1[:i]+str1[i+1:]
            b=str(a)+str(pailie(new_s))
            lis.append(b)
    return lis

print(pailie(str1))





