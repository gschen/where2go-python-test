s='0100110001010001'
l=[]
for i in range(0,len(s)+1):
    for j in range(i+1,len(s)+1):
        l.append(s[i:j])
print(len(list(set(l))))
