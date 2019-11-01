import numpy as np
import matplotlib.pyplot as plt


#解决中文显示问题
# plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
# plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

#plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']


'''
最小二乘法求解线性回归y=ax+b的参数a和b.
'''

if __name__ == '__main__':
    x = np.array([1,2,3,6,8])
    y = np.array([2,5,7,8,9])

    x_mean = np.mean(x)
    y_mean = np.mean(y)

    a_top = 0
    a_down = 0

    for x_i, y_i in zip(x,y):
        a_top += (x_i - x_mean) * (y_i - y_mean)
        a_down += (x_i - x_mean) ** 2

    a = a_top / a_down
    b = y_mean - a*x_mean

    print(a,b)
    
    y_predict = a * x + b

    plt.scatter(x,y,color='b')
    plt.plot(x, y_predict, color='r')
    plt.xlabel('Length of Pipe', fontproperties='simHei', fontsize=15)
    plt.ylabel('Price', fontproperties='simHei', fontsize=15)

    plt.show()

