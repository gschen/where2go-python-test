'''
求1+2!+3!+...+20!的和。
'''
sum,chengji = 0,1
for i in range(1,21):
    chengji*=i
    sum+=chengji
print('结果是{}'.format(sum))