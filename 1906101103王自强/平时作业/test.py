def delsapce(str):
    x,y=-1,-1
    for i in str:
        x+=1
        if i!=' ':
            m=x
            break
    for j in str[::-1]:
        y+=1
        if j!=' ':
            n=len(str)-y
            break
    return str[m:n]
print(delsapce('    5949126161    '))