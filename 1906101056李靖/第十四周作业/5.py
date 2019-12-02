#给定一个正整数N，将其表示为数字1,2,5,11相加的形式输。
def zheng(x):
    return x[::-1]==x
for i in range(100000):
    if(zheng(str(i))):
        print(i)