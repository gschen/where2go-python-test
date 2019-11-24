"""给定一个正整数N，将其表示为数字1,2,5,11相加的形式输出。 要求上述数字出现的总次数最少(每个数字可以重复使用)。
输入说明:一个正整数N (N<= 10000)。
输出说明:正整数N由1,2,5,11组成的加法表达式，要求非递增排列。
输入样例: 21
输出样例: 21=11+5+5
"""
def f1(x,l):
    if x>=11:
        l.append('11')
        return f1(x-11,l)
    elif 5<=x<11:
        l.append('5')
        return f1(x-5,l)
    elif 2<=x<5:
        l.append('2')
        return f1(x-2,l)
    elif x==1:
        l.append('1')
        return f1(x-1,l)
    else:
        return '+'.join(l)
N = int(input())
print('%d=%s'%(N,f1(N,[])))
