# 找出满足所有条件的两位数并计算其与809的乘积
for x in range(10,100):
    if 809*x == 800*x+9*x:
        if 1<=(809*x)/1000<10:
            if 1<=(8*x)/10<10:
                if 1<=(9*x)/100<10:
                    print(x,809*x)
