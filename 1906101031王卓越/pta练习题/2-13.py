votes = ["ABC","CBA","ABC","ACB","ACB"]
res=[]
j=0
l=[]
li=[]
s=[]
dic={}
while j < len(votes[0]):
    for i in range(len(votes)):
        if votes[i][j] not in dic:
            dic[votes[i][j]]=0
        dic[votes[i][j]]+=1
    res.append(dic)
    dic={} 
    j+=1
for a in res:
    max_value=0
    for x,y in a.items():
        if y>max_value:
            max_value=y
            l.insert(0,x)
        if y<max_value:
            l.append(x)
        else:
            
    li.append(l)
    l=[]
p=list(map(''.join,li))
print(''.join(p)[:len(votes[0])])
    



        

# print(res)
