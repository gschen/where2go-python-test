a,b,c=map(int,input().split(' '))
lis=[a,b,c]
max_val=max(lis)
min_val=min(lis)

#判断最大值是否为最小公倍数
justic=0
for i in lis:
    if max_val%i==0:
        pass
    else:
        justic=1
if justic==0:
    print(max_val)

#最大值不是最小公倍数，用最大值*最小值再做判断，不是就将最小值+1，重复
else:
    while True:
        new_val=max_val*min_val
        justic = 0
        for i in lis:
            if new_val % i == 0:
                pass
            else:
                justic = 1
                break
        if justic == 0:
            print(new_val)
            break
        else:
            min_val+=1

'''
用户输入：
2 4 5

程序输出：
20

'''