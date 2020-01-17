# 5.扑克牌移动
# 下面代码模拟了一套扑克牌（初始排序A~K，共13张）的操作过程。
# 操作过程是：
# 手里拿着这套扑克牌，从前面拿一张放在后面，再从前面拿一张放桌子上，再从前面拿一张
# 放在后面，....
# 如此循环操作，直到剩下最后一张牌也放在桌子上。
# 下面代码的目的就是为了求出最后桌上的牌的顺序。
# 初始的排列如果是A,2,3...K，则最后桌上的顺序为：
# [2, 4, 6, 8, 10, Q, A, 5, 9, K, 7, 3, J]


a = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
jishu = 0
shuchu = []
while a != []:
    if jishu%2 != 0:
        shuchu.append(a[0])
        a.pop(0)
        jishu += 1
    else:
        a.append(a[0])
        a.pop(0)
        jishu += 1
print(shuchu)