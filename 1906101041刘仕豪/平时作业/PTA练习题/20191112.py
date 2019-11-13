'''
一条蠕虫长1寸，在一口深为N寸的井的底部。已知蠕虫每1分钟可以向上爬U寸，但必须休息1分钟才能接着往上爬。在休息的过程
中，蠕虫又下滑了D寸。就这样，上爬和下滑重复进行。请问，蠕虫需要多长时间才能爬出井？
'''

N,U,D = map(int,input().split())
time = 0
dis = 0
while dis < N:
    dis += U
    time += 1
    if dis >= N:
        break
    dis -= D
    time += 1
print(time)




# 乌龟与兔子进行赛跑，跑场是一个矩型跑道，跑道边可以随地进行休息。乌龟每分钟可以前进3米，兔子每分钟前进9米；
# 兔子嫌乌龟跑得慢，觉得肯定能跑赢乌龟，于是，每跑10分钟回头看一下乌龟，若发现自己超过乌龟，就在路边休息，每次休息30分钟，否
# 则继续跑10分钟；而乌龟非常努力，一直跑，不休息。假定乌龟与兔子在同一起点同一时刻开始起跑，请问T分钟后乌龟和兔子谁跑得快？

T = int(input())
dist,disw,tw,ttu,temp,tmp = 0,0,0,0,0,0
disw = 3*T
for i in range(0,T):
    if (i%90>=0 and i%90<10) or (i%90>=40 and i%90<50) or (i%90>=80 and i%90<90):
        dist += 9
if disw > dist:
    print("@_@ %d"%disw)
elif disw < dist:
    print("^_^ %d"%dist)
else:
    print("-_- %d"%disw)