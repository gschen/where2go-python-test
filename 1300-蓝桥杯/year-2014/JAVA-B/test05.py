'''
7.标题：扑克序列
'''
def f(a,b,res):
    if len(b)==len(a):
        try:
            if check(b):
                res.append(b[:])
        except IndexError:
            pass
        return res
    for i in a:
        b.append(i)
        f(a,b,res)
        b.pop()


def check(b):
    id_a=[i for i,x in enumerate(b) if x=="a"]
    id_2=[i for i,x in enumerate(b) if x=="2"]
    id_3=[i for i,x in enumerate(b) if x=="3"]
    id_4=[i for i,x in enumerate(b) if x=="4"]
    if id_a[1]-id_a[0]==2 and id_2[1]-id_2[0]==3 and id_3[1]-id_3[0]==4 and id_4[1]-id_4[0]==5 and len(id_a)==2 and len(id_2)==2 and len(id_3)==2 and len(id_4)==2:
        return True
    else:
        return False
if __name__=="__main__":
    a=["a","a","2","2","3","3","4","4"]
    res=[]
    b=[]
    print(f(a,b,res))

