'''
战斗结束了，狂猎被暂时抵挡，现在当务之急就是要重整旗鼓，现在你需要帮助杰洛特点兵，规定到：
统计每一列中的士兵p {1,2,3……,n} 中符合 pi 在 p i-1 于 p i+1 之间为第二大的数字。
'''
n = int(input())
p = list(map(int,input().split()))
m = 0
for i in range(len(p)):
    if 1 <= i < len(p)-1:
        if p[i-1] < p[i] < p[i+1]: m += 1
        elif p[i+1] < p[i] < p[i-1]: m += 1
print(m)