nowtime = input("请输入现在的时间：")              #你的程序要根据起始时间和流逝的时间计算出终止时间
pasttime = input("请输入过了多少时间：")
#print(type(nowtime))
thentime = int(nowtime[-2:]) + int(pasttime)
#print(thentime)
thentime1 = nowtime[:-2]
#print(thentime1)
while thentime >= 60:
    thentime = int(thentime) -60
    thentime1 = int(thentime1) + 1
while thentime < 0:
    thentime = int(thentime) + 60
    thentime1 = int(thentime1) - 1
if thentime1 >=24:
    thentime1 = int(thentime1) - 24
if thentime1 <0:
    thentime1 = int(thentime1) + 24
print("然后是：%d%.2d"%(thentime1,thentime))
