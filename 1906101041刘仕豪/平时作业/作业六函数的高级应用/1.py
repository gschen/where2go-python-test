'''
请写一个函数，利用切片实现对字符串的首尾空格删除，不能使用str的strip()函数。
'''

def a(s):
    i=0
    k=len(s)
    if k==0:
        return s
    while i<k and s[i]==' ':
        i+=1
        if i==k:
            return s[i:]
    while s[k-1]==' ':
         k-=1
    s=s[i:k]
    return s
print(a('    adfdasgfda  '))
