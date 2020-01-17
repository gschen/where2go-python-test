def test_1(s:str)->int:
    a = '0123456789'
    if s in a or s[-1::-1] in a:
        return 5
    else:
        return 0
def test_2(s:str)->int:
    l = ['000','111','222','333','444','555','666','777','888','999']
    a = 0
    if s[1:4] in l:
        a += 3
    if s[0:3] in l:
        a+=3
    return a
def test_3(s:str)->int:
    a = 0
    if s[0]==s[1] and s[2]==s[3]:
        a+=1
    if s[0]==s[2] and s[1]==s[3]:
        a+=1
    return a
def test_4(s:str)->int:
    a = 0
    for i in s:
        if i=='6' or i == '8' or i =='9':
            a+=1
    return a
n = int(input())
num_list = []
while n > 0:
    num = input()
    num_list.append(num)
    n -= 1
for i in num_list:
    print(test_4(i)+test_3(i)+test_2(i)+test_1(i),end='\n')