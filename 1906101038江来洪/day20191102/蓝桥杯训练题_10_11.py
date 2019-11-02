#求60分钟后Y的数目
x,y = 10,90
n = 0.5
while n<=60:
    if n%1 != 0:
        y = y-x
    if n%2 == 0:
        y = y*2
    if n%3 == 0:
        x = x*2
    n += 0.5
print(y)
