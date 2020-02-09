a= input()
str =''
for i  in range(len(a)):
    if a[i:i+5]=='<text':
        for j in range(i,len(a)):
            if a[j]=='>':
                for x in range(len(a)-7):
                    if a[x]=='<':
                        str+=a[j+1:x]
                        continue
print(str)






