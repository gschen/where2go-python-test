def baa(points):
    lis1 = []
    lis2 = []
    for i in points:
        lis1.append(i[0])
        lis2.append(i[1])
    n = 0
    for j in range(len(lis1)-1):
        n += max(abs(lis1[j]-lis1[j+1]), abs(lis2[j]-lis2[j+1]))
    print(n)


baa([[1, 1], [3, 4], [-1, 0]])
