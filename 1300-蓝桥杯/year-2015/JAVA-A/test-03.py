for a in range(111,334):
    if  '0' in str(a):
        continue
    else:
        b=a*2
        c=a*3
        if '0' in str(b) or '0' in str(c):
            continue
    s=''
    s+=str(a)+str(b)+str(c)
    if sorted(list(s))==['1','2','3','4','5','6','7','8','9']:
        # print(sorted(list(s)))
        print(a)
# 192
# 219
# 273
# 327