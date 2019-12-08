'''


'''
def diyiti(n):
    n = str(n)
    su = 0
    te = 1
    for i in n:
        i = int(i)
        su += i
        te *= i
    return te-su