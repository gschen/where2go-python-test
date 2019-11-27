def jiecheng(n):
    if n == 1:
        return 1
    else:
        return n*jiecheng(n-1)
print(jiecheng(9))