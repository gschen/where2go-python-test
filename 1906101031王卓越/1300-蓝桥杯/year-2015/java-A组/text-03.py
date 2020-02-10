# 3.九数分三组
# 1~9的数字可以组成3个3位数，设为：A,B,C, 现在要求满足如下关系：
# B = 2 * A
# C = 3 * A
# 请你写出A的所有可能答案，数字间用空格分开，数字按升序排列。
for A in range(123,333):
    for B in range(A,789):
        for C in range(B,789):
            if B==2*A and C==3*A and len(set(list(str(A))))==3 and len(set(list(str(B))))==3 and len(set(list(str(C))))==3 and 0 not in list(map(int,str(A))) and 0 not in list(map(int,str(B))) and 0 not in list(map(int,str(C))):
                print(' '.join(str(A)))