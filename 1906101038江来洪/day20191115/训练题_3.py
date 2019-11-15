#小明买了多少罐啤酒
y = 0
s = 0
while True:
    for x in range(y+1):
        if x*23+y*19 == 823:
            print(x)
            s += 1
    y += 1
    if s != 0:
        break