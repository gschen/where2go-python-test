a, n = input().split()
s = 0
for i in range(1, int(n)+1):
    s += int(a*i)
print(s)
