
m,n=map(int,input().split(' '))
lis=[i for i in range(1,n)]
result_lis=[]
def opt(lis,i):
    new_lis = []

    if i==1:
        for j in range(len(lis)):
            if (j + 1) % 2 != 0:
                new_lis.append(lis[j])
        i=i+1
        opt(new_lis,i)
    else:
        if lis[i-1] > len(lis):
            # print(i,lis[i],len(lis))
            # print(lis)
            result_lis.extend(lis)
            return
        luck=lis[i-1]
        for j in range(len(lis)):
            if (j + 1) % luck != 0:
                new_lis.append(lis[j])
        i=i+1
        opt(new_lis,i)
    # print(new_lis)





opt(lis,1)
# print(result_lis)
for k in range(len(result_lis)):
    if result_lis[k]>m:
        print(len(result_lis[k:]))
        break