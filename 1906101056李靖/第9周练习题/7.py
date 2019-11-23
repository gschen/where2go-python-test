a = 100
b = 10
c = 0
d = 100
while c<b:
	d+=a
	a=a/2
	c+=1
print("第十次落地时，共经过{}米，第十次反弹{}米。".format(d,a))