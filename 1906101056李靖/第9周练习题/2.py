import math
for x in range(1, 10000):
    a = int(math.sqrt(x + 100))
    b = int(math.sqrt(x + 268))
    if a ** 2 == x + 100 and b ** 2 == x + 268:
        print(x)
