'''
1.有以下代码
[x*x for x in range(10)]
（1）	请用切片取出第一个元素
（2）	请用切片取出最后一个元素
（3）	请用切片取出第二个到第五个元素
（4）	请用切片取出除了第一个元素的剩下所有元素
（5）	请用切片取出除了最后一个元素的所有元素
'''
l = [x*x for x in range(10)]
print(l[0])
print(l[-1])
print(l[1:5])
print(l[1:])
print(l[:-1])