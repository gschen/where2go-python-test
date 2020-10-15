n = int(input())
s = list(map(int,input().split(" ")))
sum = 0
while len(s)>1:
    x1 = min(s)
    s.remove(x1)
    x2 = min(s)
    s.remove(x2)
    p = x1+x2
    sum += p
    s.append(p)
print(sum)

