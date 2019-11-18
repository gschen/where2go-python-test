"""
3.有一个数列（1，2，2，4，……），第一项为1，第二项为2，第三项为前面两项的乘积，请使用生成器，并且打印出前10项。
"""
def shu(x):
    b,c = 1,2
    while x >0:
        x -= 1
        yield b
        b, c = c, c * b
mm = int(input())
print([i for i in shu(mm)])