'''
啤酒2.3元，饮料1.9元。一共花了82.3元。
啤酒数量比饮料少。
问：啤酒数量
'''
for m in range(35):
    for n in range(40):
        if m < n and m*2.3 + n*1.9 == 82.3:
            print(m)