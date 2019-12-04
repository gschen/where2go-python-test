a = 2
b = 1
sum = 0
for i in range(20):
    sum = a / b + sum
    a, b = (a + b), a
print(sum)
