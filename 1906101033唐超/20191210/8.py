'''
本题要求编写程序，计算序列 1 + 1/3 + 1/5 + ... 的前N项之和。
输入格式:
输入在一行中给出一个正整数N。
'''

N=int(input())
s = 0
for i in range(1,N+1):
    s += 1/(2*i-1)
s = str(s)
s=s[:16]
s=float(s)
print("sum=%.6f"%s)