'''
一根拉面
对折一次后中间切一刀，得到3根
对折两次后中间切一刀，得到5根
对折三次后中间切一刀，得到9根
问：对折十次后能得到多少根
'''
def qiemiantiao(n):
    miantiao = 2
    for i in range(n):
        miantiao = miantiao*2 - 1
    print(miantiao)



qiemiantiao(10)