def add(ls):
    sum=0
    for i in ls:
        sum+=i
    return sum
a = [90,80,60]
b = [80,60,30]
c = [80,70,90]
result = map(add,[a,b,c])
for i in result:
        print(i)