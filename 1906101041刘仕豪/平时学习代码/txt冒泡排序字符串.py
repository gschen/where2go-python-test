def suiji():
    import random
    letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    l=[]
    n=0
    while n<20:
        x=random.randint(0,51)
        l.append(letter[x])
        n+=1
    #print(1)
    n=0
    while n<20:
        str2 = ''
        while len(str2)<2:
            x=random.randint(0,51)
            str2+=letter[x]
        l.append(str2)
        n+=1
    #print(2)
    n=0
    while n<20:
        str3 = ''
        while len(str3)<3:
            x=random.randint(0,51)
            str3+=letter[x]
        l.append(str3)
        n+=1
    #print(3)
    n=0
    while n<20:
        str4 = ''
        while len(str4)<4:
            x=random.randint(0,51)
            str4+=letter[x]
        l.append(str4)
        n+=1
    #print(4)
    n=0
    while n<20:
        str5 = ''
        while len(str5)<5:
            x=random.randint(0,51)
            str5+=letter[x]
        l.append(str5)
        n+=1
    #print(5)
    n=0
    while n<20:
        str6 = ''
        while len(str6)<6:
            x=random.randint(0,51)
            str6+=letter[x]
        l.append(str6)
        n+=1
    #print(6)
    n=0
    while n<20:
        str7 = ''
        while len(str7)<7:
            x=random.randint(0,51)
            str7+=letter[x]
        l.append(str7)
        n+=1
    #print(7)
    n=0
    while n<20:
        str8 = ''
        while len(str8)<8:
            x=random.randint(0,51)
            str8+=letter[x]
        l.append(str8)
        n+=1
    #print(8)
    n=0
    while n<20:
        str9 = ''
        while len(str9)<9:
            x=random.randint(0,51)
            str9+=letter[x]
        l.append(str9)
        n+=1
    #print(9)
    #print(l)
    return l
file = open("C:/Users/刘仕豪/Desktop/a.txt",'w')
ranstr = suiji()
for s in ranstr:
    file.write(s)
    file.write('\n')
file.close()
#先随机创建一个有许多字符串的txt文档

file2 = open(r"C:/Users/刘仕豪/Desktop/a.txt")
strs = []
for line in file2:
    strs.append(line)
for i in range(len(strs)-1):
    for j in range(len(strs)-i):
        if (j<len(strs)-i-1):
            if strs[j]>strs[j+1]:
                strs[j],strs[j+1]=strs[j+1],strs[j]
file3 = open("C:/Users/刘仕豪/Desktop/finished.txt",'w')
for k in strs:
    file3.write(k)
    file3.write('\n')
file2.close()
file3.close()
