# 给定两个字符串，均只包含英文字母,需区分大小写,一个是源字符串SS(长度<1000),另-个是目标.字符串TS(长度<1000)
# 请问能否通过删除SS中的字符(不改变顺序)将它变换成TS,如果可以输出"YES" ,不可以则输出"NO"
s = str(input())
list1 = [i for i in str(input())]
m = 0
for n in list1:
    if n in s:
        m += 1
if m == len(list1):
    d = 0
    print('yes')
    if d != 0:
        print('no')