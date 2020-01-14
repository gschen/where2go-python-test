'''

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''

result = []

# 判断生成的括号是否符合要求
def is_valid(track):

    stack = []

    for i in track:
        if i == '(':
            stack.append(i)
        elif len(stack) == 0:
            return False
        else:
            stack.pop()

    if len(stack) == 0:
        return True

    return False

'''
算法基本思想：
先用回溯法生产所有的括号，然后
'''
def backtrack(n, track):
    
    if len(track) == 2*n:

        if is_valid(track):
            print(track)
            result.append(list(track))
        return
    
    # 利用回溯法生成所有的情况
    for i in ['(', ')']:

        track.append(i)
        backtrack(n, track)
        track.pop()


backtrack(3, [])

r = []
for line in result:
    r.append(''.join(line))

print(r)