year = 1999
week = 5
while year%100 != 99 or week != 7:
    if year%100 == 0 and year%400 == 0 or year%100 != 0 and year%4 == 0:
        week += 366%7
    else:
        week += 365%7
    if week > 7:
        week = week%7
    year += 1
print(year)

