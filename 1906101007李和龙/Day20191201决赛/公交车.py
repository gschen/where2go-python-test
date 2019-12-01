num = int(input())
list1 = []
for i in range(num):
    a,b,c = map(str,input().split())
    time1 = int(c) - int(b)
    if time1<0:
        time1 = 1200+time1
    list1.append(time1)
max_time = max(list1)

str_time = str(max_time)

hour = int(str_time[:1])

if int(str_time[1:])> 60:
    fen = int(str_time[1:])-40
else:
    fen = int(str_time[1:])

print("%dH%dM"%(hour,fen))