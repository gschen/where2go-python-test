def sixteen_eigen(n):
    # 先将16进制数转为2进制数
    two_str=''
    for x in range(len(n)):
        if n[x]=='A':
            value=10
        elif n[x]=='B':
            value=11
        elif n[x]=='C':
            value=12
        elif n[x]=='D':
            value=13
        elif n[x]=='E':
            value=14
        elif n[x]=='F':
            value=15
        else:
            value=eval(n[x])
        for i in range(0,2):
            for ii in range(0, 2):
                for iii in range(0, 2):
                    for iiii in range(0, 2):
                        if 8*i+4*ii+2*iii+1*iiii==value:
                            two_str=two_str+str(i)+str(ii)+str(iii)+str(iiii)
    print(two_str)
    #二进制转十进制
    ten=0
    for y in range(len(two_str)):
        ten=ten+eval(two_str[-(y-1)])*(2**y)
    #二进制转八进制
    # if len(two_str)%3==0:
    #     pass
    # else:
    #     m=len(two_str)%3
    #     two_str='0'*(3-m)+two_str
    # eight=''
    # #print(two_str)
    # for j in range(0,len(two_str)-2,3):
    #     if j==0 and two_str[j+1]=='0' and two_str[j+2]=='0':
    #         pass
    #     else:
    #         eight=eight+str((eval(two_str[j])*4+eval(two_str[j+1])*2+eval(two_str[j+2])*1))
    return ten

print(sixteen_eigen('1E'))



