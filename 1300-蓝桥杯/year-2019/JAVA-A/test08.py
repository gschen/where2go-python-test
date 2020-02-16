def main():
    lis = []
    #number=[0]
    def process(x):
        #number[0]=number[0]+1
        x=int(x)
        if x not in lis:
            lis.append(x)
        else:
            while True:
                #print('测试', x)
                x=x+1
                if x not in lis:
                    lis.append(x)
                    break

    n=eval(input())

    lis.extend(map(process,input().split(' ')))
    for i in lis:
        if i==None:
            continue
        else:
            print(i,end=' ')

    #print(number)

main()
'''
测试用例
5
2 1 1 3 4
result:2 1 3 4 5

'''