#未完成

def main():
    import itertools
    # INPUT
    n = eval(input())
    lis=[]
    lis.extend(map(int,input().split(' ')))
    if len(lis)!=n:
        return 'error'


    number=n-1
    total_condition=[]
    k=0
    while k<=n:
        k+=1
        for i in itertools.permutations(lis,k):
            i=sorted(i)
            if i not in total_condition and i[0]==1:
                total_condition.append(i)
                if i[-1]-i[0]+1==len(i):
                    #print(i)
                    number+=1
    print(number)
main()

'''
示例：
用户输入：
4
3 2 4 1

程序应输出：
7

用户输入：
5
3 4 2 5 1

程序应输出：
9


'''