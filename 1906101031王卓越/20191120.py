def raw(k):
    if len(k)%2!=0:
        print("flase")
    else:
        x=0
        while x<len(k)/2:
            if k[x]=='[' or k[x]==']' or k[x]=='(' or k[x]==')' or k[x]=='{' or k[x]=='}' :
                if k[x]=='[' and k[x+1]==']' or k[x+1]=='[' and k[x]==']' or k[x]=='{' and k[x+1]=='}'  or k[x+1]=='{' and k[x]=='}' or k[x]=='(' and k[x+1]==')' or k[x+1]=='(' and k[x]==')':
                    x+=2
                    p=1
                    continue
                else:
                    r=0
                    while r<len(k)/2:
                        if k[r]=='[' and k[-r-1]==']' or k[-r-1]=='[' and k[r]==']' or k[r]=='{' and k[-r-1]=='}'  or k[-r-1]=='{' and k[r]=='}' or k[r]=='(' and k[-r-1]==')' or k[-r-1]=='(' and k[r]==')':
                            r+=1
                            p=1
                            continue
                        else:
                            p=0
                            break                            
        if p==0:
            print("false")
        elif p==1:
            print("true")
print(raw("(ftghfg){()}"))
