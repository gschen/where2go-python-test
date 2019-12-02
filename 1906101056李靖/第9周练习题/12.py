n = input('请输入一个五位以内的正整数:')
num = 0
for i in n:
	if '0'<=i<='9':
		num=num+1
print('它是一个{}位数，逆序为{}'.format(num,n[::-1]))