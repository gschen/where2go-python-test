# 3.三羊献瑞
# •	观察下面的加法算式：
#       祥 瑞 生 辉  +   三 羊 献 瑞
# ----------------------------
#    三 羊 生 瑞 气
# •	其中，相同的汉字代表相同的数字，不同的汉字代表不同的数字。
# •	请你填写“三羊献瑞”所代表的4位数字（答案唯一），不要填写任何多余内容。
for a in range(1,10):# a代表三
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                for e in range(0,10):
                    for f in range(0,10):
                        for g in range(0,10):
                            for h in range(0,10):
                                li=[a,b,c,d,e,f,g,h]
                                if len(set(li))==8 :
                                    s=a*10000+b*1000+c*100+d*10+e
                                    x=f*1000+d*100+c*10+g
                                    y=a*1000+b*100+h*10+d
                                    if s==x+y:
                                        print(y)
                                       
                                        