#有一个集合L={'Jack':[90,80,60],'Machile':[80,60,30],'Bob':[80,70,90]},
#请使用map分别计算每个同学的
#（1）总成绩
#（2）平均分
#王卓越
def raw(x,y,z):
    return x+y+z
def rkw(x,y,z):
    return x+y+z/3
a=[90,80,80]
b=[80,60,70]
c=[60,30,90]
k=list(map(raw,a,b,c))
s=list(map(rkw,a,b,c))
print(k,s)


