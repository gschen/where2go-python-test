for i in range(1,3):
    for j in range(10):
        for h in range(10):
            for q in range(10):
                for w in range(3):
                    for e in range(1,10):
                        r=i*10000000+j*1000000+h*100000+q*10000++6*100+w*10+e
                        if r%2012==0 and r%3==0 and r%12==0:
                            print(r)