jishu=[1,1]
oushu=[0,1]
for i in range(1,40):
    if i==1 or i==2:
        continue
    else:
        js=oushu[-1]+oushu[-2]
        os=jishu[-1]+jishu[-2]
        jishu.append(js)
        oushu.append(os)
print(oushu[-1])