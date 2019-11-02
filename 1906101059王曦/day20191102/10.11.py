n = 0
x = 10
y = 90
while n <= 60:
    if n % 0.5==0 and n != int(n):
        y = y - x
    if n % 2 == 0 and n != 0:
            y = y * 2
    if n % 3 == 0 and n != 0:
        x = x * 2
    n = n + 0.5
print(y)
