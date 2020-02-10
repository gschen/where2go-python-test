n,r =input().split(' ')
lis=[]
for i in range(eval(n)):
    lis.append(list(map(int,input().split(','))))#用列表将坐标存起来
print(lis)
def buyu(lis,r):
    mini = 0
    maxm=0
    all=[]
    dic={}
    for i in range(len(lis)):
        fash_lis=[]
        for j in range(i+1,len(lis)):
            if (lis[i][0]-lis[j][0])**2 + (lis[i][1]-lis[j][1])**2 <int(r)**2:
                fash_lis.append(lis[j])
                maxm+=1
            else:
                pass
        dic[i] = maxm
        all.append(fash_lis)
    #获取字典中最大值的键
    index=sorted(dic.items(),key=lambda x:x[1], reverse=True)
    getfish=all[list(index[0])]
    for i in getfish:
        lis.remove(i)
    mini+=1
    if len(lis)==0:
        return mini
    else:
        return buyu(lis,r)
print(buyu(lis,r))






















