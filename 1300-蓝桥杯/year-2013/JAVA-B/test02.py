numbers=0
for a in range(1,10):
    for b in range(1, 10):
        if b==a:
            continue
        for c in range(1, 10):
            if c==b or c==a:
                continue
            for d in range(1, 10):
                if d==c or d==b or d==a:
                    continue
                for e in range(1, 10):
                    if e==a or e==b or e==c or e==d:
                        continue
                    elif (a*10+b)*(c*100+d*10+e)==(c * 10 + e) * (a * 100 + d * 10 + b):
                        numbers+=1
print(numbers)

