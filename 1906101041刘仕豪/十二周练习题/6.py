'''
找零钱问题：假设只有 1 分、 2 分、五分、 1 角、二角、 五角、 1元的硬币。在超市结账 时，如果 需要找零钱，
收银员希望将最少的硬币数找给顾客。那么，给定 需要找的零钱数目，如何求得最少的硬币数呢？
'''

def tanxin():
    d = [0.01,0.02,0.05,0.1,0.2,0.5,1.0]
    d_num = []
    s = 0
    temp = input('请输入每种零钱的数量：')
    d_num0 = temp.split(" ")
    for i in range(0, len(d_num0)):
        d_num.append(int(d_num0[i]))
        s += d[i] * d_num[i]
        sum = float(input("请输入需要找的零钱:"))
        if sum > s:
            print("数据有错")
            return 0
        s = s - sum
        i = 6
        while i >= 0:
            if sum >= d[i]:
                n = int(sum / d[i])
                if n >= d_num[i]:
                    n = d_num[i]
                    sum -= n * d[i]
                    print("用了%d个%f元硬币" % (n, d[i]))
tanxin()