'''计算1到M (含M)之间的合数数量,输出其值。
输入说明: 一个正整数M (M < 10000)。
输出说明:输出合数的数量。
输入样例: 12
输出样例: 6
'''
M=int(input())
x=0
for i in range(1,M+1):
    for j in range(2,i):
        if i%j==0:
            x+=1
            break
print(x)