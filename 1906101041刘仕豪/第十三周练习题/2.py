'''
16.计算1到M (含M)之间的合数数量,输出其值。
输入说明: 一个正整数M (M < 10000)。
输出说明:输出合数的数量。
输入样例: 12
输出样例: 6
'''
def heshu(m):
    list_a = []
    for i in range(2,m+1):
         for j in range(2,i):
            if i % j == 0 :
                list_a.append(i)
                break
    return list_a
M = int(input())
print(len(heshu(M)))