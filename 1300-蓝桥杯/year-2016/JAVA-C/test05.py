import itertools
number=0
for i in itertools.permutations('0123456789',10):
    aim_str=[]
    for j in i:
        aim_str.append(int(j))
    part1=aim_str[0]
    part2= aim_str[1:3]
    part3 = aim_str[3:6]
    part4 = aim_str[6:]
    if sum(part4)>sum(part3)>sum(part2)>part1:
        number+=1
print(number)