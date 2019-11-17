#列出所有可能的海盗人数
for a in range(4,21):
    for b in range (1,a):
        for c in range(1,b):
            for d in range(1,c):
                e = 0
                if 1/a+1/b+1/c+1/d == 1:
                    print(a,b,c,d,e)