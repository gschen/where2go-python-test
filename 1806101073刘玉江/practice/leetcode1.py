def canMeasureWater(x, y, z):
    def gcd(num1, num2):
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        return num1

    res = gcd(x, y)
    if z % res == 0:
        return True
    else:
        return False


print(canMeasureWater(2, 6, 5))
