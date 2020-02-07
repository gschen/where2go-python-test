a=[2,0,1,9]
b=[]
for i in range(1,2020):
    i=str(i)
    for ii in i:
        if int(ii) in a:
            b.append(int(i))
            break
        else:
            pass
print(sum(b))
