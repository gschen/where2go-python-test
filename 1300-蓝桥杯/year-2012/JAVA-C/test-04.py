dic={'}':'{',']':'[',')':'('}
zkh,ykh=dic.values(),dic.keys()
def khpp(x):
    lis=[]
    c=0
    while True:
        for i in x:
            if i in zkh:
                lis.append(i)
            elif i in ykh:
                if lis==[]:
                    print('false')
                    c+=1
                    return False

                else:
                    if lis[-1]==dic[i]:
                        lis.pop(-1)
                    else:
                        print('false')
                        c+=1
                        return False
            else:
                continue
        break
    if c==0:
        if lis==[]:
            print('true')
        else:
            print('false')

khpp('(d{{x}(xsd)x({sax}{{}s(())}sssd)}()()()')