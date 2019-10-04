#将分式化为最简分式
import fractions
x,y = map(int,input('请随便输入一个分数：').split('/'))
i = fractions.gcd(x,y)
m = x/i
n = y/i
print(str('%.0f'% m)+'/'+str('%.0f'% n))