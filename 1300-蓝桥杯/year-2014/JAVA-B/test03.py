'''
3.标题：猜字母
'''
def s(ls):
    if len(ls)==1:
        return ls
    else:
        for i in range(len(ls)):
            if i%2==0:
                ls[i]="z"
        strs=str(ls)
        strs.replace("z","")
        ls=list(strs)
        s(ls)
strs=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]*106
print(s(strs))

