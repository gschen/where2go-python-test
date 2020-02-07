count=0
s=1543

while s>1:
    if s%2!=0:
        s-=1    
        count+=1
    else:s=s/2
print(count+1)