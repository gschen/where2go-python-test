

'''
                  1
    黄金数 = ---------------------
                        1
             1 + -----------------
                          1
                 1 + -------------
                            1
                     1 + ---------
                          1 + ...
n1=1/1=1/1
n2=1/(1+1/1)=1/2
n3=1/(1+1/(1+1/1))=2/3
n4=1/(1+1/(1+1/(1+1/1)))=3/5
。。。。
分子为头两项为1，1 的斐波拉契数列
分母为头两项为1，2 的斐波拉契数列
'''
def fbolie(n):

    a=1
    b=1

    #分子为a+b,分母为b+c
    for i in range(n-1):
        c=b

        b=a+b
        a = c
    return a,b


#模拟除法过程，四舍五入保留n位小数
def get_chushu(a,b,n):
    qz=a//b
    qy=a%b
    result='{}.'.format(qz)
    i=0
    #将产生n+1位小数
    while  i<=n:
        i+=1
        qz=qy*10//b
        qy=qy*10%b
        result+=str(qz)
    result=list(result)
    end_val=int(result[-1])
    if end_val>4:
        for j in range(-2,-len(result),-1):
            if int(result[j])>8:
                result[j]='0'
            else:
                result[j]=str(int(result[j])+1)
                break

    return ''.join(result[:-1])
a,b=fbolie(250)

result=get_chushu(a,b,100)
print(result)