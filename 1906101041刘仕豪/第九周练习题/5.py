'''
5、	判断101-200之间有多少个素数，并输出所有素数。
'''

a = []
print("101-200之间的素数有：")
for b in range(101,201):
    if b%2!=0 and b%3!=0 and b%5!=0:
        a.append(b)
        print(b)
print("共{}个素数".format(len(a)))