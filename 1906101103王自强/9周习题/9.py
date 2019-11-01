'''9、	两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人
。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x
,z比，请编程序找出三队赛手的名单'''

l=['x','y','z']
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i!=0 and k!=0 and k!=2and i!=j and j!=k and i!=k:
                print('a对{}，b对{}，c对{}'.format(l[i],l[j],l[k]))