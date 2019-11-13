from functools import reduce
L={'Jack':[90,80,60],'Machile':[80,60,30],'Bob':[80,70,90]}
def add(x,y):
    return x+y
totalscore=(reduce(add, L['Jack']))
print(totalscore)
n=len(L['Jack'])
averagescore=totalscore//n
print(averagescore)
print('1906101103 王自强')