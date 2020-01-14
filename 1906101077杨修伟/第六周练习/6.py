n = int(input())
m = False
for x in range(100):
    for y in range(100):
        if x<=y and x*x+y*y == n:
            print("%d %d" % (x,y))
            m = True
if m == False:
    print("No Solution")