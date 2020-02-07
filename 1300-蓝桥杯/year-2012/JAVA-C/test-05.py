start = list(map(str,input().split()))
end = []
for i in range(12):
    end.append(start[i*2:][1])
    start.append(start[i*2:][0])
end.append(start[11*2+1:][1])
print(end)
