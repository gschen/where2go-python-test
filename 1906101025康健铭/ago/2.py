from datetime import datetime
kjm=datetime(2000,4,13)
print(kjm.isoformat())
print(kjm.year,"年",kjm.month,"月",kjm.day,"日")
print(kjm.day,"日",kjm.month,"月",kjm.year,"年")
print(kjm.strftime("%Y-%m-%d"))
print(kjm.strftime("%d-%m-%Y"))
print(kjm.strftime("%Y:%m:%d"))
print(kjm.strftime("%Y=%m=%d"))
print(kjm.strftime("%Y/%m?%d"))
print("{0:%Y}年{0:%m}月{0:%d}日".format(kjm))
print("{0:%d}日{0:%m}月{0:%Y}年".format(kjm))

