count =0
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                for e in range(1,10):
                    for f in range(1,10):
                        for g in range(1,10):
                            for h in range(1,10):
                                for i in range(1,10):
                                    if a != b and a != c and a != d and a != e and a != f and a != g and a != h and a != i and\
                                            b != c and b != d and b != e and b != f and b != g and b != h and b != i and \
                                            c != d and  c != e and c != f and c != g and c != h and c != i and\
                                            d != e and d != f and d != g and d != h and d != i and\
                                            e != f and e != g and e != h and e != i and\
                                            f != g and f != h and f != i and\
                                            g != h and g != i and \
                                            h != i:
                                        print(a,b,c,d,e,f,g,h,i)
                                        if a+b+d+f==a+c+e+i and a+c+e+i==f+g+h+i and f+g+h+i==a+b+d+f:
                                            count +=1
print(count/6)