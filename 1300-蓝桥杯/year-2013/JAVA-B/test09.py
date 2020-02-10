import itertools
n=input()
n_len=len(n)
n=eval(n)

a='123456789'
lis=[]


def test02():
    numbers = 0  # 统计满足条件的次数

    all_condition=[]
    for i in range(1,n_len+1):
        for j in range(1,8):
            for k in range(1,8):
                if i+j+k==9:
                    all_condition.append([i,j,k])

    for i in itertools.permutations(a,9):
        i_str=''.join(i)
        for j in all_condition:
            first=int(i_str[:j[0]])
            if first>=n:
                continue
            else:
                second=int(i_str[j[0]:j[1]+j[0]])
                three=int(i_str[j[1]+j[0]:])
                # print('测试',first,second,three)
                if first+(second/three)==n:

                    numbers+=1
    return numbers
print(test02())
'''
例如：
用户输入：
100
程序输出：
11

再例如：
用户输入：
105
程序输出：
6

'''