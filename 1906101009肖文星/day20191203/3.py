def L(a):
    x = []
    y = []#创建两个空列表
    for m in a:#把大列表中的小列表取出来
        x.append(m[0])
        y.append(m[1])#循环遍历小列表，取出x和y分别装在一个列表里
    time=0
    for n in range(len(x)-1):#做坐标个数减一次循环运算
            x1 = abs(x[n]-x[n+1])#依次算相邻两个点横坐标之差的绝对值
            y1 = abs(y[n]-y[n+1])#依次算相邻两个点纵坐标之差的绝对值
            time += max(x1,y1)#利用max函数比较大小，并累加
    print(time)#打印时间
L([[1,1],[3,4],[-1,0]])