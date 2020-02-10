import itertools
number=0
for i in itertools.permutations('123456789',5):
    a,b,c,d,e=i[0],i[1],i[2],i[3],i[4]
    if eval(a+b)*eval(c+d+e)==eval(a+d+b)*eval(c+e):
        number+=1
print(number)

