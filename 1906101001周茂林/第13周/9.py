'''
字母连连看,给定一个由小写英文字母组成的字符串(长度 <1000),如果字符串中有两个连续的字母相同，
则这两个字母可同时消除，并不断重复该操作，直到不能消除为止。请编程判断该字符串是否可以完全消除。
输入说明:一个字符串。
输出说明:如果可以完全消除，输出"YES" ,如果不可以,输出消除后的结果。
输入样例1: abacddcaba
输出样例1: YES
输入样例2: asdfghhgf
输出样例2: asd
'''
def shanchu(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s.pop(i)
            s.pop(i)
            return shanchu(s)
s = list(input())
shanchu(s)
if len(s) == 0:
    print('YES')
else:
    print(''.join(s))
