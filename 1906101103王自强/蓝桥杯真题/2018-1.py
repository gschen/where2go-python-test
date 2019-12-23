'''2000年的1月1日，是那一年的第1天。
那么，2000年的m月n日，是那一年的第几天？
注意：需要提交的是一个整数，不要填写任何多余内容。'''
def fun(m,n):
    sum=n
    print(sum)
    for i in range(1,m):
        if i<=7:
            if i%2==1:
                sum+=31
            if i==2:
                sum+=29
            if i%2==0 and i!=2:
                sum+=30
        print(i,sum)
        if i>7:
            if i%2==1:
                sum+=30
            if i%2==0:
                sum+=31
    return sum
print(fun(5,4))