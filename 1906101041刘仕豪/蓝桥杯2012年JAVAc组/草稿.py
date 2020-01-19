# a = ord('a')
# b = ord('b')
# c = ord('b')+ord('a')
# print(a,b,c)
# print(eval('12+3'))
def num_sum(n):
    while len(str(n))!=1:
        a = 0
        n = str(n)
        for i in n:
            a +=int(i)
        n = a
    return n
s = '4321'
a = '0123456789'
if s in a or s[-1::-1] in a:
    print(5)