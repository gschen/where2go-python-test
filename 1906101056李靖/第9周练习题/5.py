n=2
for i in range(101,200):
    while i>n:
        if i%n==0:
            break
        else:
            n+=1
    if n==i:
        print(i)
