"""
def pi(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*pi(n-1)

a = eval(input())
b = 1
c = 0
sum = 0
jieguo = 1
while jieguo >=a:
    jieguo = pi(c)/b
    c += 1
    b = b*(2*c+1)
    sum = sum + jieguo
    if jieguo<a:
        break
print("{:.6f}".format(sum*2))

"""

def pi(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * pi(n - 1)

a = eval(input("请输入："))
b = 1
c = 0
sum = 0
jieguo = 1
while True:

    if jieguo >= a:
        jieguo = pi(c) / b
        c += 1
        b = b * (2 * c + 1)
        sum = sum + jieguo
    else:
        break
print("{:.6f}".format(sum * 2))


