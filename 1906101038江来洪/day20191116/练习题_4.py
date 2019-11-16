#对折10次后的面条中间切一刀后一共有多少根面条
def jiang(x):
    if x == 0:
        return 2
    else:
        s = 2
        for i in range(x):
            s = s*2-1
        return s
print(jiang(10))