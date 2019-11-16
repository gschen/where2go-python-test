'''
杰洛特与一种猎魔人在前方抵抗狂猎大军，现在，该女巫发挥自己的用处了，两位树桩菇娘分别在城楼上发动了魔法，但释放魔法需要瞄准，而你也只知道一个大概，因此，需要你利用卷积的知识运算来辅助瞄准。
    分别给定一个自定义大小的原始矩阵和一个3*3卷积核矩阵(不需要翻转，直接原样求)，你所做的就是通过这两个矩阵求出卷积后的输出矩阵。
    PS:请使用0来补全原矩阵，(防止python引用框架答题答题)不要使用边缘拷贝的方式
如果你不知道怎么求卷积，这里有一个举例：
    给定一个3*3的原始矩阵h
    h = [ 1 , 2 , 3]
        [ 1 , 1 , 1]
        [ 0 , 1 , 2]
    给定一个3*3的卷积核v
    v = [ 1 , 0 , 1]
        [ 2 , 1 , 1]
        [ 0 , 0 , 0]
    那么卷积运算 h * v = ans ，ans为卷积运算的输出矩阵
    对于每一个ans而言有 ans [i,j] = sum( h[i-a,j-b]*v[a,b] )
    ans的第一行第一列的结果为： 0*1 + 0*0 + 0*1 + 0*2 + 1*1 + 2*1 + 0*0 + 1*0 + 1*0 = 3
    ans的第二行第二列的结果为： 1*1 + 2*0 + 3*1 + 1*2 + 1*1 + 1*1 + 0*0 + 1*0 + 2*0 = 8
    因此，卷积后的输出矩阵为：
    ans=[3 , 7 , 7]
        [4 , 8 , 5]
        [2 , 5 , 5]
'''
m,n = map(int,input().split())
h = []
for i in range(m):
    la = input().split()
    for j in la:
        h.append(j)
v = []
for i in range(m):
    la = input().split()
    for j in la:
        v.append(j)
ans = [x for x in range(m*n)]

# 周围包一圈0
for j in range(n,1,-1):
    for i in [0,0]:
        h.insert(j * m,i)
adh = [0 for x in range(m + 3)]
h.extend(adh)
for i in adh:
    h.insert(0,i)

ll = [x for x in range(len(h))]
for i in range(1,n):
    ll.pop(i*m)
    ll.pop(i*m)
print(ll)
for i,k in zip(range(m*n),ll):
    print(i,'>>>>>>>')
    print(k,']]]]]]')
    for j in range(9):
        ans[i] += int(v[j]) * int(h[k])
        k += 1
    print(ans[i],'??????')

print('ans=',end='')
for i in range(len(ans)):
    if i % m == 0 and i != 0:
        print('\n','   ',end='')
    print(ans[i],end='  ')
