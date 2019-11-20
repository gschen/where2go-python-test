def xwx(L):
    if L == []:
        return (None, None)
    else:
        min, max = L[0], L[0]
        for i in L:
            if min > i:
             min = i
            if max < i:
                max = i
        return (max, min)
L = [1, 2, 5.9, 67, 3]
print(xwx(L))