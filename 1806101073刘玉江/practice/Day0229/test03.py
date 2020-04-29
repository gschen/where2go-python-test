import datetime
time1 = datetime.datetime.now()
def fb(n):
    while(n>2):
        return fb(n-1)+fb(n-2)
    else:
        return 1
listx=[]
for i in range(1,35):
    listx.append(fb(i))
print(listx)
time2 = datetime.datetime.now()
print(time2-time1)