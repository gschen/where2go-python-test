def raw(a,b,c):
    from datetime import datetime
    s=datetime(a,b,c)
    x=s.strftime("%a-%b-%c")
    y=s.strftime("%a.%b.%c")
    z=s.strftime("%a,%b,%c")
    j=s.strftime("%a/%b/%c")
    k=s.strftime("%a~%b~%c")
    l=s.strftime("%a:%b:%c")
    print("我的生日是%ddd" % a,b,c)
    print("我出生与%d "% a,b,c)
    print("%d那天是我的生日" % a,b,c)
    return s,x,y,z,j,k,l
a,b,c=map(int,input("请输入你的出生年份：").split())
print(raw(a,b,c))
#王卓越