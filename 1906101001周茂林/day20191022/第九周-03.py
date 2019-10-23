'''
输入三个整数x,y,z，请把这三个数由小到大输出。
'''
x,y,z = map(int,input().split())
a = min(x,y,z)
b = max(x,y,z)
print(a,x+y+z-a-b,b)