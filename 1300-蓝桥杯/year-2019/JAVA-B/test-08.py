K=int(input())
s=input()
S=s.split(" ")
print(S)
res=0
for i in range(len(S)):
    if S[i]=='Alice':
        for j in range(i+1,len(S)):
            if S[j]=='Bob' or S[j]=='Bob.':
                sum=1
                for k in range(i+1,j):
                    sum+=len(S[k])+1
                if sum<=K:
                    res+=1

for i in range(len(S)):
    if S[i]=='Bob' or S[i]=='Bob.':
        for j in range(i+1,len(S)):
            if S[j]=='Alice':
                sum=1
                for k in range(i+1,j):
                    sum+=len(S[k])+1
                if sum<=K:
                    res+=1

print(res)