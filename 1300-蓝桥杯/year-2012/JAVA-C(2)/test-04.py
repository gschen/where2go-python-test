# 4.括号问题
# 下面的代码用于判断一个串中的括号是否匹配
# 所谓匹配是指不同类型的括号必须左右呼应，可以相互包含，但不能交叉
# 例如：
# ..(..[..]..).. 是允许的
# ..(...[...)....].... 是禁止的
# 对于 main 方法中的测试用例，应该输出：
# false
# true
# false
# false

#>>>>>>>>>方法一
s = input()
kuohao = ['(',')','[',']','{','}']
kuohao_list = []
for i in s:
    if i in kuohao:
        kuohao_list.append(i)
kuohao_str = ''.join(kuohao_list)
l = []
for i in kuohao_str:
    if i == '(' or i =='[' or i == '{':
        l.append(i)
    elif i == ')' and l[-1] == '(':
        l.pop()
    elif i == ']' and l[-1] == '[':
        l.pop()
    elif i == '}' and l[-1] == '{':
        l.pop()
print(len(l)==0)



#>>>>>>>>>方法二
a = input()
zuo = ['(','[','{','<']
you = [')',']','}','>']
A = []
for i in a:
    if i in zuo:
        A.append(i)
    if i in you:
        if i == you[zuo.index(A[-1])]:
            A.pop()
        else:
            break
if A == []:
    print(True)
else:
    print(False)