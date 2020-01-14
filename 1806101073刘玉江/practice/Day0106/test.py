import time
start_time = time.time()

a = 0
b = 0
c = 0
for i in range(1001):
    a = a+1
    b = 0
    c = 0
    for k in range(1001):
        b = b +1
        c = 0
        for l in range(1001):
            c = c +1
            print(i//10,'%')
            if a*a + b*b == c*c and a+b+c == 1000:
                print(a,"",b,"",c,"")


end_time = time.time()

print('time:',end_time-start_time)




