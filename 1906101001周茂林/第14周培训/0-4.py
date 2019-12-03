'''
给定一个正整数N，将其表示为数字1,2,5,11相加的形式输出。 要求上述数字出现的总次数最少(每个数字可以重复使用)。
输入说明:一个正整数N (N<= 10000)。
输出说明:正整数N由1,2,5,11组成的加法表达式，要求非递增排列。
输入样例:
21
输出样例:
11
5
5
1
'''


def fenjie(n):
    for i in lis[::-1]:               #使用for循环遍历列表，注意列表要逆序遍历
        while n >= i:                 #这里使用while循环保证列表里的元素能被多次使用
            n -= i
            print(i)



lis = [1,2,5,11]
fenjie(int(input()))