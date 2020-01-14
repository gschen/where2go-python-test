def firstdigit(x):
    lis=[]
    for i in x:
        if i.isdigit():
            print(i)
            lis.append(i)
            break
        else:
            continue
    if lis==[]:
        print('-1')
firstdigit('asd123')
firstdigit('122')
firstdigit('ads')