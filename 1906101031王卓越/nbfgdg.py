i=['a','b','c','d']
for x in i:
	for y in i:
		for z in i:
			if (x!=z) and (x!=y) and (z!=y):
				print(x,y,z)