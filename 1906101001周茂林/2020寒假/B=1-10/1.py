'''
世纪末的星期
    曾有邪教称1999年12月31日是世界末日。当然该谣言已经不攻自破。
    还有人称今后的某个世纪末的12月31日，如果是星期一则会....
    有趣的是，任何一个世纪末的年份的12月31日都不可能是星期一!!
    于是，“谣言制造商”又修改为星期日......
    1999年的12月31日是星期五，请问：未来哪一个离我们最近的一个世纪末年（即xx99年）的12月31日正好是星期天（即星期日）？
    请回答该年份（只写这个4位整数，不要写12月31等多余信息）
'''
n = 5
for i in range(2000, 9999):
    if i % 4 == 0 and i % 100 != 0:
        n += 366
    elif i % 4 == 0 and i % 400 == 0:
        n += 366
    else:
        n += 365
    n %= 7
    if n == 0 and (i-1999) % 100 == 0:
        print(i)
        break

