def main():
    n=eval(input())
    lis=[]
    lis.extend(map(int,input().split(' ')))
    print(lis)
    if len(lis)!=n:
        return 'error'
    else:
        lis.reverse()

        i=0
        max_val=0
        min_deep=0
        while len(lis)>0:

            sum_val=0
            for i in range(2**i):
                if len(lis)==0:
                    break
                sum_val+=lis.pop()
            if sum_val>max_val:
                max_val=sum_val
                min_deep = i + 1
            i=i+1
        print(min_deep,max_val)

main()
#测试用例
'''
7
1 6 5 4 3 2 1
result:2
'''