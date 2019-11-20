"""
16.计算1到M (含M)之间的合数数量,输出其值。（和数与质数相反）
输入说明: 一个正整数M (M < 10000)。
输出说明:输出合数的数量。
输入样例: 12
输出样例: 6

"""
def heshu(x):
    q = set()
    for a in range(2,x+1):
        for b in range(2,x):
            if (a % b == 0) and a != b:
                q.add(a)
    return len(q)
m = int(input())
print(heshu(m))