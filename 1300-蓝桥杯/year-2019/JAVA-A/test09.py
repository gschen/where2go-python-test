def main():

    import itertools

    #input_process
    n,m,k=map(int,input().split(' '))
    all_ct=[]
    for i in range(n):
        sc_in=[]
        sc_in.extend(map(int,input().split(' ')))
        all_ct.append(sc_in)
    i=0
    while i<=n:

        #从1到n对排列所有组合
        i+=1
        for j in itertools.permutations(all_ct,i):
            new_condition=[]
            for k in j:

                new_condition.extend(k)

            #去掉组合中重复的元素
            new_condition=set(new_condition)

            if len(new_condition)==m:

                print(i)
                return i


main()
'''
【样例输入】
6 5 3
1 1 2
1 2 3
1 1 3
2 3 5
5 4 2
5 1 2
【样例输出】
2

'''