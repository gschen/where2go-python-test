def fib(n):
	n = int(input('请输入你想得到的第几项数'))
	a,b = 0,1
	m = 0
	while m<n-2:
		a,b = b,a+b
		m += 1
	if n == 1:
		b = 0
	print(b)
fib(9)