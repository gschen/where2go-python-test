'''循环节长度
两个整数做除法，有时会产生循环小数，其循环部分称为：循环节。
比如，11/13=6=>0.846153846153.....  其循环节为[846153] 共有6位。
下面的方法，可以求出循环节的长度。
'''
a,b=map(int,input().split('/'))
s=str(a/b)
x=False
for j in range(2,len(s)):
    for i in range(1,b+1):
        if s[j:j+i]==s[j+i:j+2*i]:
            x=True
            print(i)
            break
    if x==True:
        break