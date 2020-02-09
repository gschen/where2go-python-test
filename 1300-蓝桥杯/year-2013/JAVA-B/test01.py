n=1999
days=5 #该年的最后一天是星期5
#判断平年和闰年 闰年366、平年365
while True:
    n+=1
    #闰年366
    if n%100!=0 and n%4==0:
        days=((366%7+days)**2)**0.5
        if days>7:
            days=days%7
        if days==7 and n%100==99:
            print(n)
            break
        else:
            continue
    elif n%100==0 and n%400==0:
        days = ((366 % 7 + days) ** 2) ** 0.5
        if days > 7:
            days = days % 7
        if days == 7 and n%100==99:
            print(n)
            break
        else:
            continue
    #平年365
    else:
        days = ((365 % 7 + days) ** 2) ** 0.5
        if days > 7:
            days = days % 7
        if days == 7 and n%100==99:
            print(n)
            break
        else:
            continue