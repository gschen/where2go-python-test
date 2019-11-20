'''
给定两个字符串，均只包含英文字母,需区分大小写,一个是源字符串SS(长度<1000),另-个是目标.字符串TS(长度<1000)
请问能否通过删除SS中的字符(不改变顺序)将它变换成TS,如果可以输出"YES" ,不可以则输出"NO"
输入说明:第一行为源字符串SS,第二行为目标字符串TS。
输出说明:可以输出"YES" ，不可以输出"NO" 。
输入样例1: Thereisacomputer
          Treat
输出样例1: YES
输入样例2: Thereisacomputer
          Trait
输出样例2: NO
'''
SS = input()
TS = input()
s = []
for i in TS:
    for j in range(len(SS)):
        if i == SS[j]:
            s.append(SS[j])
            SS = SS[j+1:]
            break
if TS == ''.join(s):
    print('YES')
else:
    print('NO')
