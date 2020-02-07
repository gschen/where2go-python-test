'''
匪警请拨110,即使手机欠费也可拨通！
为了保障社会秩序，保护人民群众生命财产安全，警察叔叔需要与罪犯斗智斗勇，因而需要
经常性地进行体力训练和智力训练！

某批警察叔叔正在进行智力训练：

1 2 3 4 5 6 7 8 9 = 110;

请看上边的算式，为了使等式成立，需要在数字间填入加号或者减号（可以不填，但不能
填入其它符号）。之间没有填入符号的数字组合成一个数，例如：12+34+56+7-8+9 就是一种合格
的填法；123+4+5+67-89 是另一个可能的答案。

请你利用计算机的优势，帮助警察叔叔快速找到所有答案。

* 程序输出：

每个答案占一行。形如：

12+34+56+7-8+9
123+4+5+67-89
......

已知的两个答案可以输出，但不计分。
各个答案的前后顺序不重要。

注意：

请仔细调试！您的程序只有能运行出正确结果的时候才有机会得分！

'''
#由于时间复杂度为3的8次方，可以直接遍历

lis = ['','+','-']
for aa in lis:
    a = '1'+aa+'2'
    for bb in lis:
        b = a+bb+'3'
        for cc in lis:
            c = b+cc+'4'
            for dd in lis:
                d = c+dd+'5'
                for ee in lis:
                    e = d+ee+'6'
                    for ff in lis:
                        f = e+ff+'7'
                        for gg in lis:
                            g = f+gg+'8'
                            for hh in lis:
                                h = g+hh+'9'
                                if eval(h) == 110:
                                    print(h,end='\n')
