sum_val=[]
#第n层就是1到n的和
for i in range(1,101):
    s=0
    #第n层的煤球数量
    for j in range(1,i+1):
        s+=j
    sum_val.append(s)
print(sum(sum_val))