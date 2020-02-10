a = [
    ['UDDLUULRUL'],
    ['UURLLLRRRU'],
    ['RRUURLDLRD'],
    ['RUDDDDUUUU'],
    ['URUDLLRRUU'],
    ['DURLRLDLRL'],
    ['ULLURLLRDU'],
    ['RDLULLRDDD'],
    ['UUDDUDUDLL'],
    ['ULRDLUURRR']
]


def m(y, x):
    global li
    global count
    print(y,x)
    if [y,x] not in li:
        li.append([y, x])
        if 0 <= x < 10 and 0 <= y < 10:
            fx = a[y][x]
            if fx == 'U':
                m(y - 1, x)
            elif fx == 'D':
                m(y + 1, x)
            elif fx == 'L':
                m(y, x - 1)
            else:
                m(y, x + 1)
        else:
            count +=1
            return
    else:
        return

count = 0
for y in range(10):
    for x in range(10):
        li = []
        m(y,x)

print(count)
# while x:
#     if a == ['U']:
#         lambda x, y: (x + 1, y)  # 向上
#     if a == ['D']:
#         lambda x, y: (x - 1, y)  # 向下
#     if a == ['R']:
#         lambda x, y: (x, y + 1)  # 向右
#     if a == ['L']:
#         lambda x, y: (x, y - 1)  # 向左
#     break
# print(x)




