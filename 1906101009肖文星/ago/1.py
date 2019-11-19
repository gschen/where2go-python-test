'''
有四个字母：a、b、c、d，能组成多少个互不相同且无重复三位字符串？输出所有结果。
'''
p1='abcd'
n = 0
for z in p1:
	for x in p1:
		for v in p1:
			if z != x and z != v and x != v:
				n = n + 1
				print(z,x,v)
print('一共有{}个'.format(n))

