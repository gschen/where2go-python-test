from datetime import timedelta, datetime
a,b,c = map(int,input("请输入开始时间(以.间隔)：").split("."))
d,e,f = map(int,input("请输入结束时间(以.间隔)：").split("."))
delta = datetime(d,e,f) -datetime(a,b,c)
print(delta)
