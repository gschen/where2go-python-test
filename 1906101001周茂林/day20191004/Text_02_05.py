n = float(input())
x = 1
s = 0
while x <= n:
    y = 1/x
    s += y
    x += 2
print(round(s,6))