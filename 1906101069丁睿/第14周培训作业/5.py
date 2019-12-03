M=[]
for i in range(1,100001):
        i = str(i)
        n = i[::-1]
        if i == n:
            i = int(i)
            M.append(i)
print(M)
