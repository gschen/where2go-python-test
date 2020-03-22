def generateTheString(n):
    res = ""
    if n % 2 == 1:
        for i in range(n):
            res = res + "x"
    else:
        for i in range(n-1):
            res = res + "y"
        res = res + "x"
    return res



print(generateTheString(6))