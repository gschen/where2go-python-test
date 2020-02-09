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