'''
统计1到N (含)之间所有平方数的个数,并输出这个数目。
提示:平方数的个数,如4是2的平方数, 16是4的平方数，5不是平方数。
输入说明: 一个整数N(N< 100000);
输出说明:平方数的个数
输入样例: 50
输出样例: 7
'''
def pingfang(n):
    m = 0
    for i in range(1,n+1):
        if i**2 <= n:
            m += 1
    print(m)


pingfang(50)