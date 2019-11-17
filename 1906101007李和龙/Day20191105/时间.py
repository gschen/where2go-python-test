#如果a+b+c=1000,并且a**2+b**2=c**2,求abc的组合
import time
start_time = time.time()
# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             if a + b + c == 1000 and a**2 + b**2 == c**2:
#                 print("a,b,c:%d,%d,%d"%(a,b,c))



for a in range(1001):
    for b in range(1001):
        # for c in range(1001):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print("a,b,c:%d,%d,%d"%(a,b,c))

end_time = time.time()
used_time= end_time - start_time
print(used_time)
