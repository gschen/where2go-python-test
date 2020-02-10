import itertools
number=0
hitory=[]

#对1949四位数用全排列
for i in itertools.permutations('1949',4):
    aim_str=''.join(i)

    #因为1949里有相同的数字，全排列也会出现相同的数字，需要做排除
    if aim_str not in hitory:
        hitory.append(aim_str)
    else:
        continue

    if aim_str=='9491':
        continue
    else:
        #0为初始状态，表示该数是素数
        justic=0

        for j in range(2,20):
            if eval(aim_str)%j==0:
                #1表示该数不是是素数
                justic=1
                break
        if justic==0:
            # print(aim_str)
            number+=1
# print(hitory)
print(number)

