x=int(input('员工入职年数：'))
y=int(input('周工作时间:'))
if x>=5 and y<=40:
        i=y*50
if x>=5 and y>40:
        i=40*50+(y-40)*50*3/2
if x<5 and y<=40:
        i=y*30
if x<5 and y>40:
        i=40*30+(y-40)*30*3/2
print("%.2f" %i)





