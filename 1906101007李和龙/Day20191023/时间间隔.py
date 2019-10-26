day1 =[1,31,59,90,120,151,181,212,243,273,304,334,365]                #每个月前面天数的总和  平年
day2 =[1,31,60,91,121,152,182,213,244,274,305,335,366]                     #闰年

year,month,day = map(int,input("请输入开始年月日(以.隔开):").split("."))
if year % 100 == 0:

    if year % 400 == 0:
        kaishi = 366-(day2[month - 1] + day)
    if year % 400 != 0:
        kaishi = 365-(day1[month - 1] + day)
else:

    if year % 4 == 0:
        kaishi = 366-(day2[month - 1] + day)
    else:
        kaishi = 365-(day1[month - 1] + day)        #第一年剩下的天数


#print(kaishi)

year1,month1,dayy = map(int,input("请输入结束年月日(以.隔开):").split("."))

if year % 100 == 0:

    if year1 % 400 == 0:
        jieshu = day2[month1 - 1] + dayy
    if year1 % 400 != 0:
        jieshu = day1[month1 - 1] + dayy
else:

    if year1 % 4 == 0:
        jieshu = day2[month1 - 1] + dayy
    else:
        jieshu = day1[month1 - 1] + dayy          # 最后一年过了的天数



#print(jieshu)

runnian = 0
pingnian = 0
if year != year1:
    for i in range(year + 1,year1):
        if i % 100 == 0:
            if i % 400 == 0:
                runnian += 1
            else:
                pingnian += 1
        else:                                         # 区别中间年份的闰年和平年
            if i % 4 == 0:
                runnian += 1
            else:
                pingnian += 1
#print(runnian,pingnian)
    zongday = runnian*366 + pingnian*365 + jieshu + kaishi    # 总天数等于闰年+平年+第一年剩余的 + 最后一年过去的天数
else:
    if year1 %100 == 0:
        if year1 % 400 == 0:
            zongday = jieshu - (366-kaishi)
        else:
            zongday = jieshu - (365 - kaishi)
    else:
        if year1 % 4 == 0:
            zongday = jieshu - (366 - kaishi)
        else:
            zongday = jieshu - (365 - kaishi)

print("两时间间隔%d天"%zongday)




#判断是闰年还是平年决定是365 还是366天
