# def calculate_postfix(postfix):
# 	    stack = []	# 用list模拟栈的后进先出
# 	    for p in postfix:
# 	        if p in '+-x/':  # operator
# 	            value_2 = int(stack.pop())	# 第二个操作数
# 	            value_1 = int(stack.pop())	# 第一个操作数
# 	            if p == '+':
# 	                result = value_1 + value_2
# 	            elif p == '-':
# 	                result = value_1 - value_2
# 	            elif p == 'x':
# 	                result = value_1 * value_2
# 	            else:	# 整除
# 	                result = value_1 // value_2
# 	            stack.append(result)
# 	        else:
# 	            stack.append(p)

def self(N,M):
	nums=[]
	com=[]
	n=N+M+1
	N>0>M
	for i in range(n):
		print(i)
		sorted(nums,nums+n,com)
	for i in range(n):
		if i<0:
			nums[i]=-nums[i];
		if (M):
			for i in range(n-M):
				nums[i]=-nums[i];
	for i in range(n):
		nums+=nums[i];
		return 0


