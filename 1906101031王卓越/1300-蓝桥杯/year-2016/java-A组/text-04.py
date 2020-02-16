# 第四题：寒假作业
# 题目描述
# 现在小学的数学题目也不是那么好玩的。
# 看看这个寒假作业：

#    □ + □ = □
#    □ - □ = □
#    □ × □ = □
#    □ ÷ □ = □
   
#    (如果显示不出来，可以参见【图1.jpg】)
   
# 每个方块代表1~13中的某一个数字，但不能重复。
# 比如：
#  6  + 7 = 13
#  9  - 8 = 1
#  3  * 4 = 12
#  10 / 2 = 5

# 以及： 
#  7  + 6 = 13
#  9  - 8 = 1
#  3  * 4 = 12
#  10 / 2 = 5

# 就算两种解法。（加法，乘法交换律后算不同的方案）
 
# 你一共找到了多少种方案？


# 请填写表示方案数目的整数。
# 注意：你提交的应该是一个整数，不要填写任何多余的内容或说明性文字。
num=0
for a in range(1,14):
    for b in range(1,14):
        for c in range(3,14):
            if a+b==c and len(set([a,b,c]))==3:
                for d in range(3,14):
                    for e in range(1,14):
                        for f in range(1,14):
                            if d-e==f and len(set([a,b,c,d,e,f]))==6 :
                                for g in range(2,14):
                                    for h in range(2,14):
                                        for i in range(6,14):
                                            if  g*h==i and len(set([a,b,c,d,e,f,g,h,i]))==9:
                                                for j in range(6,14):
                                                    for k in range(2,14):
                                                        for l in range(2,14):
                                                            if j/k==l and len(set([a,b,c,d,e,f,g,h,i,j,k,l]))==12:
                                                                num+=1
print(num)