#输入：一个整数n，表示开始购买的饮料数量（0<n<10000）
#输出：一个整数，表示实际得到的饮料数
def sumdreak(n):
    res = 0
    while n > 3 :#当瓶数大于3时，执行循环
        res+=3#每喝掉三瓶记录一次
        n-=2#喝掉三瓶时可以换一瓶
    res=res+n
    return res

print(sumdreak(100))



