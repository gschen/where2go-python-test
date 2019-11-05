'''
请利用map()函数，写函数可以把英文名字规范化，比如输入['adam', 'LISA', 'barT'] 输出['Adam', 'Lisa', 'Bart']
'''

l=['adam', 'LISA', 'barT']
l2=list(map(str.capitalize,l))
print(l2)