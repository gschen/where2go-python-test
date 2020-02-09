n = int(input("n:"))
R = list(map(int, input().split(' ')))
sum = 0
for i in range(n-1):
    if R[i] != i+1:
        a = R[R[i]-1]
        R[R[i]-1] = R[i]
        R[i] = a

        sum += 1
print(sum)