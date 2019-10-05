m,n = map(int,input().split())
sum = 0
while m <= n:
    sum += m**2 + 1/m
    m += 1
print(round(sum,6))