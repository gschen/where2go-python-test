'''递增三元组
给定三个整数数组
A = [A1, A2, ... AN], 
B = [B1, B2, ... BN], 
C = [C1, C2, ... CN]，
请你统计有多少个三元组(i, j, k) 满足：
1. 1 <= i, j, k <= N  
2. Ai < Bj < Ck  
【输入格式】
第一行包含一个整数N。
第二行包含N个整数A1, A2, ... AN。
第三行包含N个整数B1, B2, ... BN。
第四行包含N个整数C1, C2, ... CN。
对于30%的数据，1 <= N <= 100  
对于60%的数据，1 <= N <= 1000 
对于100%的数据，1 <= N <= 100000 0 <= Ai, Bi, Ci <= 100000 
【输出格式】
一个整数表示答案
【输入样例】
3
1 1 1
2 2 2
3 3 3
5'''
N=int(input())
A=list(map(int,input().split(' ')))
B=list(map(int,input().split(' ')))
C=list(map(int,input().split(' ')))
sum=0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if A[i]<B[j]<C[k]:
                sum+=1
print(sum)