from math import *
x=0
while x<10000000:
	x=x+1
	k=x+100
	z=x+268
	g=sqrt(k)
	h=sqrt(z)
	if round(g)!=g and round(h)!=h:
		print(x)
		break
		
