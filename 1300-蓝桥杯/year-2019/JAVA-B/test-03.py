def shulie(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n==3:
        return 1
    else:
        return shulie(n-3)+shulie(n-2)+shulie(n-1)
print(shulie(20190324))
