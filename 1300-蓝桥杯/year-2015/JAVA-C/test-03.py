# coding=utf-8

'''
第三题：无穷分数
题目描述
无穷的分数，有时会趋向于固定的数字。
请计算【图1.jpg】所示的无穷分数，要求四舍五入，精确到小数点后5位，小数位不足的补0。

请填写该浮点数，不能填写任何多余的内容。

'''
# (思路：用round函数就可以做到四舍五入了,再用format把不足的补充好就可以了,还有就是word里似乎没有图片，就用这个输入了)
n=eval(input('请输入这个无穷分数：'))
print('{:0<.5f}'.format(round(n,5)))