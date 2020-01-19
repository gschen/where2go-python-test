'''
第一个函数递归算法求阶乘
'''
def cc(x):
    if x==1:
        return 1
    return x*cc(x-1)
print(cc(6))