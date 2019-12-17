m, n = map(int, input().split())
lis = [x**2 + 1/x for x in range(m, n+1)]
print(round(sum(lis), 6))
