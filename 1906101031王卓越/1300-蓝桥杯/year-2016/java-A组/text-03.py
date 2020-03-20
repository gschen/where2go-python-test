# 第三题：搭积木
# 题目描述
# 小明最近喜欢搭数字积木，
# 一共有10块积木，每个积木上有一个数字，0~9。

# 搭积木规则：
# 每个积木放到其它两个积木的上面，并且一定比下面的两个积木数字小。
# 最后搭成4层的金字塔形，必须用完所有的积木。

# 下面是两种合格的搭法：

#    0
#   1 2
#  3 4 5
# 6 7 8 9

#    0
#   3 1
#  7 5 2
# 9 8 6 4    

# 请你计算这样的搭法一共有多少种？

# 请填表示总数目的数字。
# 注意：你提交的应该是一个整数，不要填写任何多余的内容或说明性文字。
num=0
for a in range(1,5):
    for b in range(1,5):
        if len(set(list([a,b])))==2:
            for c in range(max(2,a),8):
                for e in range(max(2,b),8):
                    for d in range(max(3,a,b),8):
                        if len(set(list([a,b,c,d,e])))==5:
                            for f in range(max(3,c),10):
                                for i in range(max(3,e),10):
                                    for g in range(max(d,c,5),10):
                                        for h in range(max(d,e,5),10):
                                            if len(set(list([a,b,c,d,e,f,g,h,i])))==9:
                                                print('   {}   '.format(0))
                                                print('  {} {}  '.format(a,b))
                                                print(' {} {} {} '.format(c,d,e))
                                                print('{} {} {} {}'.format(f,g,h,i))
                                                num+=1
print(num)

        
                                                                                                                                                                                                                                                                             
            






