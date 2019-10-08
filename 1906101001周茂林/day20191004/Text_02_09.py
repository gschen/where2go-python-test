a,b,c = map(int,input().split())
d = sorted([a,b,c])
print('{}->{}->{}'.format(int(d[0]),int(d[1]),int(d[2])))