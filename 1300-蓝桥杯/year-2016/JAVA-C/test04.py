import itertools
number=0
for i in itertools.permutations('123456789',9):
    aim_str=''.join(i)
    if eval(aim_str[0])+(eval(aim_str[1])*eval(aim_str[6:])+eval(aim_str[3:6])*eval(aim_str[2]))//\
            (eval(aim_str[2])*eval(aim_str[6:]))==10:
        number+=1
print(number)