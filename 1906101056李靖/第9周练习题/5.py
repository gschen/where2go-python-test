for x in range(1,10):
	for y in range(0,10):
		for z in range(0,10):
			m=x**3+y**3+z**3
			n=x*100+y*10+z
			if m==n:
				print(m)