lower, upper = map(int, input().split())
if lower >= upper or upper >= 100:
    print('Invalid')
else:
    print("fahr  celsius")
    for i in range(lower, upper+1, 2):
        print(i, '  ', round(5*(i-32)/9, 1))
