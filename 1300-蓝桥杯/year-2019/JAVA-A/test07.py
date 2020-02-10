def main():
    #input
    n,m,t=map(int,input().split(' '))
    lis={}
    for i in range(m):
        a,b=map(int,input().split(' '))
        #1处于优先缓存中，0则相反
        if a>=5:
            lis[b]=1
        else:
            lis[b] = 0
    number=0
    for i in lis:
        if lis[i]==1:
            number+=1
    print(number)





main()
'''
测试用例
2 6 6
1 1
5 2
3 1
6 2
2 1
6 2
result:1
'''