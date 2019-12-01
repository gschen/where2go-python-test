def jiecheng(x):
    if x==1:
        return 1
    return x*jiecheng(x-1)
print(jiecheng(3))
