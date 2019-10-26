'''
9、	两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单
'''
a=1
b=2
c=3
for x in range(1,4):
    for y in range(1, 4):
        for z in range(1, 4):
            if x!=1 and x!=3 and z!=3 and x!=y and y!=z and x!=z:
                print("令a,b,c分别为1，2，3，则x对应{}，y对应{}，z对应{}。".format(x,y,z))

