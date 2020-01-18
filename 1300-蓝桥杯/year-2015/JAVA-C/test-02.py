sum_nuber = 0
for i in range(1,26):
    n=str(i**3)
    s=str(i)
    l=len(s)
    if eval(n[-l:])==i and eval(n[-l])!=0:
        sum_nuber+=1
print(sum_nuber)


