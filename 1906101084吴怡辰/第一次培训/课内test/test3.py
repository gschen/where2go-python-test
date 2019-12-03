for A in range(0,10):
    for B in range(0,10):
        for C in range(0,10):
            for D in range(0,10):
                for E in range(0,10):
                    if A!=B and A!=C and A!=D and A!=E and B!=C and B!=D and B!=E and C!=D and C!=E and D!=E:
                        if (E*10000+D*1000+C*100+B*10+A)%(A*10000+B*1000+C*100+D*10+E)==0:
                            print(A*10000+B*1000+C*100+D*10+E)