a,b =input().split(' ')
b=int(b)
lis = list(map(int, input().split()))
lis0=[]#定义一个列表，存放小强记得看过的电影的序号
for i in range(len(lis)):
    if len(lis0)<b:#当列表中电影数量未达到小强的遗忘量时，将电影序号加入列表
        lis0.append(lis[i])
    else:#当列表中达到饱和时，需要判断当前电影序号是否在列表中，如果在，则pass，不在则将该序号加入列表，并删除记得最后的哪一个电影序号
        if (lis[i] not in lis0):
            lis0.append(lis[i])
            del lis0[0]
        else:
            pass











