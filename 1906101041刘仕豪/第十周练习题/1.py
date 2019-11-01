'''
1、	求100之内的素数。（素数：只能被1和本身整除的数）
'''
def sushu(n):
    a=[]
    for x in range(0,n):
        if x%2!=0 and x%3!=0 and x%5!=0 or x==2 or x==3 or x==5:
            a.append(x)
    print(a)
sushu(100)
