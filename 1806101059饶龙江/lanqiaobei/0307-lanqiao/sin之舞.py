def An(i,n):#求An表达式的函数，
    if i==n:#递归出口，最后一项
        return 'sin'+'('+str(n)+')'
    else:
        return 'sin'+'('+str(i)+'+'+str((-1)**i)+str(An(i+1,n))+')'#连接通项公式，开始递归

def Sn(n,j):#求Sn表达式的函数
    if j==n:#递归出口，翻转后Sn的第一项
        return str(n)+'+'+str(An(1,1))
    else:
        return str(j)+'+'+str(An(1,n+1-j))+'('+str(Sn(n,j+1))+')'#开始递归，需要将An（）放入递归中
print(Sn(3,1))




