for n in range(1,21):
    for a in range(1,20):
        for b in range(1,19):
            for c in range(1,18):
                if 1/n+1/a+1/b+1/c==1 and n>a and a>b and b>c:
                    print("{},{},{},{},0".format(n,a,b,c))

'''if语句段暂时不懂'''