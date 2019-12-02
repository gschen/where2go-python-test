#小明是个急性子，上小学的时候经常把老师写在黑板. 上的题目抄错了。有一次,老师出的题目是:36x495=?他却给抄成了: 396 x45 = ?但结果却很戏剧性，他的答案竟然是对的! !
#假设abcd e代表1~9不同的5个数字(注意是各不相同的数字，且不含0)
#能满足形如: ab* cde = adb * ce这样的算式-共有多少种?


z = 0
for a in range(1,10):
    for b in range(1,10):
        for c in range(1, 10):
            for d in range(1, 10):
                for e in range(1, 10):
                    if (a*10+b)*(c*100+d*10+e) == (a*100+d*10+b)*(c*10+e) and a!=b and a!=c and a!=d and a!=e and b!=c and b!=d and b!=e and c!=d and c!=e and d!=e:
                        z+=1
print(z)