'''给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差'''
def subtractProductAndSum(n):
    x=str(n)
    he=0
    ji=1
    for i in x:
        he+=int(i)
        ji*=int(i)
    return (ji-he)
