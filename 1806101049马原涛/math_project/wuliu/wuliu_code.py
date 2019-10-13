import csv
import math
import numpy as np
import sys

sys.setrecursionlimit(100000) #迭代次数上限设置
#文件读取，grap地图信息，data基本信息
#data   序号	  门店	经度	   纬度	 规定时间窗起	  规定时间窗终	可接受时间窗起  可接受时间窗终 	需求量t	服务时间min
csv_file = csv.reader(open('grap.csv', 'r'))
csv_file1 = csv.reader(open('data.csv', 'r'))
csv_file2 = csv.reader(open('grap_number.csv', 'r'))
csv_file3 = csv.reader(open('reference.csv', 'r'))
data=[]
grap = []
grap_number=[]
reference=[]
grap_number.clear()
grap.clear()
data.clear()
'''for u in range(len(grap)):
    grap_number.append(grap[u])
print(grap_number)'''

for line in csv_file:
    grap.append(line)

for line in csv_file1:
    data.append(line)

for line in csv_file2:
    data.append(line)
    grap_number.append(line)

for line in csv_file3:
    reference.append(line)


#数据类型转换
for i in range(len(grap)):
    for j in range(len(grap[i])):
        grap[i][j]=float(grap[i][j])
for i in  range(len(data)):
    for j in range(len(data[i])):
        if j>=4:
            data[i][j]=float(data[i][j])
for i in range(len(reference)):
    for j in range(len(reference[i])):
        reference[i][j]=float(reference[i][j])


#数值定义
n_aver=0.9
g=9.8
C_r=0.01
B=1.7
v=35
P_aux=1500
M=float('inf')
aerfa_c=-10
beta_c=-0.05
aerfa=45
c_aver=250
aerfa1=0.002
aerfa2=0.004
c_e=10
ce_=14
p=8000#冷链产品单位价格

quelity=3 #空车重量
R=36000#能源，单位w/h


start_time=0#发车次数






aaa=0
def rout():
    number = 0 #迭代次数
    start = 0
    distance = 0
    # 初始化变量

    history = []  # 记录所有车的行驶路径
    drive_history = []  # 单个车的行程记录
    t_history = []
    while len(grap_number[0])>1:
        number+=1
        if start==0:

            mix_value =999
            #选出第一个点
            mix_index=0
            for i in range(len(grap[start])):#0-20

                if grap[start][i]<mix_value:
                    mix_value=grap[start][i]
                    mix_index=i
            history.append(start)
            start=mix_index
            distance=grap[0][start]

            #grap1减少一列
            for j in range(len(grap)):
                del grap_number[j][1]


            #改变对应列的值
            for k in range(len(grap)):
                grap[k][start]=999


            t_serve = data[start - 1][9] / 60

            t_end = data[start - 1][4] + t_serve







    #非起点
        else:

            list_index=[]
            list_index.clear()
            mix_index=0
            mix_value=999
            #找到满足时间窗的点
            for i in range(len(grap[start])):
                t_drive=grap[start][i]/v
                t_done=t_end+t_drive
                if data[start-1][4]<=t_done<=data[start-1][5]:
                    list_index.append(i)
                else:
                    pass
            #如果没有满足最优时间窗的点就直接结束本次循环，重新从起点开始
            if len(list_index)==0:

                history.append(start)
                start=0

                continue
            else:
                history.append(start)
                # 从满足时间窗的点里选出距离最小的
                for j in range(len(list_index)):

                    if grap[start][list_index[j]]<mix_value:

                        mix_value=grap[start][list_index[j]]
                        mix_index=list_index[j]
            start=mix_index
            distance=mix_value
                # grap1减少一列

            for j in range(len(grap)):
                del grap_number[j][1]

                # 改变对应列的值
            for k in range(0,21):

                grap[k][start] = 999
    duoyu=[]
    for i in range(len(grap)):
        if i in history:
            pass
        else:
            duoyu.append(i)
    for i in range(len(duoyu)):
        if history[-1]==0:
            history.append(duoyu[0])
            del duoyu[0]
        else:
            history.append(0)
            history.append(duoyu[0])
            del duoyu[0]
    return history,number



#数据分离
def one_route(history):
    total_history=[]
    frequeny=len(history)
    last_i = 0
    for i in range(1,frequeny):

        list_route = []

        if history[i]==0:

            for j in range(last_i,i):
                list_route.append(history[j])


            total_history.append(list_route)
            last_i=i
    kis=0
    for k in range(len(total_history)):
        for y in range(len(total_history[k])):
            kis+=1

    list_route=[]
    for k in range(len(history)-kis):
        list_route.append(history[kis])
        kis+=1

    total_history.append(list_route)
    for b in range(len(total_history)):
        total_history[b].append(0)
    return total_history


#得出每条路线的载货量
def wij_list(total_history):
    w_ij=[]
    for i in range(len(total_history)):
        list_ones=[]
        for j in range(len(total_history[i])):
            if total_history[i][j]==0:
                pass
            else:
                wij=data[total_history[i][j]-1][8]
                list_ones.append(wij)
        w_ij.append(list_ones)
    #w_ij每条路线载货记录
    #tw_ij是w_ij的颠倒,并求累计重量
    tw_ij=[]
    for i in range(len(w_ij)):
        list_reserve=[]
        for j in range(len(w_ij[i])):
            list_reserve.append(w_ij[i][len(w_ij[i])-1-j])
        #累计重量
        tw_ij.append(np.cumsum(list_reserve))

    goods=[]
    for i in range(len(tw_ij)):
        list_reserve=[]
        for j in range(len(tw_ij[i])):
            list_reserve.append(tw_ij[i][j])
        goods.append(list_reserve)
    goods_l=[]
    for i in range(len(goods)):
        list_reserve=[]
        for j in range(len(goods[i])):
            list_reserve.append(goods[i][len(goods[i])-1-j])
        list_reserve.append(0)
        goods_l.append(list_reserve)

    return goods_l
#时间计算
def time_give(total_history):
    time_list=[]
    time_list_start=[]
    for i in range(0,len(total_history)):

        start_time=0
        h_time=0
        for j in range(len(total_history[i])):
            if j == 0:
                pass
            elif j==1:
                #计算车辆出发时间
                guid_time=data[total_history[i][1]][4]#规定时间
                distance=reference[0][total_history[i][1]]
                drive_time=distance/v
                start_time=guid_time-drive_time
                time_list_start.append(start_time)
            elif j>1 and total_history[i][j]!=0:
                #计算后续点所花时间：行驶时间+服务时间
                #距离为上一个的total_history[i][j-1]到下一个点total_history[i][j]的距离
                distance=reference[total_history[i][j-1]][total_history[i][j]]
                drive_time=distance/v
                fuwu_time=data[total_history[i][j]-1][9]/60 #服务时间

                h_time+=drive_time+fuwu_time
            elif j>1 and total_history[i][j]==0:
                distance=distance=reference[total_history[i][j-1]][total_history[i][j]]
                drive_time=distance/v
                h_time+=drive_time
        time_list.append(h_time)
    return time_list,time_list_start



#能源消耗函数
def energy_cost(total_history,wij_list):
    eij_total=[]
    distance_list=[]
    for i in range(len(total_history)):
        eij_one = []
        for j in range(len(total_history[i])-1):
            last=total_history[i][j]
            next=total_history[i][j+1]
            wij=wij_list[i][j]+3 #货物重量加空车质量，单位t
            distance=reference[last][next]
            distance_list.append(distance)

            y = 9.8 * distance * 0.01 / (0.9*3.6)
            beta = 1.7 * distance * 35 * 35 /(0.9*3.6*3.6*3.6)

            #print(beta)
            eij=y * wij + beta

            #print("{}*{}+{}*{}".format(y,wij,beta,distance))
            eij_one.append(eij)
        eij_total.append(sum(eij_one)+P_aux*time_list[i])

    return eij_total,distance_list


def energy_judge(eij_total,total_history):
    judge=[]
    for i in  eij_total:
        zw=R>i
        judge.append(zw)
    cishu=0
    for j in judge:
        if j !=True:
            cishu+=1
    if cishu==0:
        print("所有路线均成立")
        cost_calculation(total_history)
    else:
        print("部分路线不成立，输出新路线")
        #输出不成立路线的在能源消耗列表中的索引
        false=list(eij_total).index(False)
        #对不成立路线进行折半拆分
        false_list=[]

        for k in range(len(total_history[false])//2,len(total_history[false])):
            false_list.append(total_history[false][k])
        for k in range(len(total_history[false])//2,len(total_history[false])):
            del total_history[false][k]

        total_history.append(false_list)
        wijlist=wij_list(total_history)
        time_list, time_list_start = time_give(total_history)
        eij_total = energy_cost(total_history,wijlist)
        energy_judge(eij_total,total_history)

def cost_calculation(total_history):
    #服务时间，与total_history一一对应
    fu_list=[]
    #total_history的一维列表
    dian_list=[]
    #需求列表，与服务时间和路线一一对应
    demand_list=[]
    #距离列表，与上述一一对应
    dis_list=[]
    dis_list.append(0)
    #每个点所载货物列表
    huowu_list=[]
    for i in range(len(total_history)):
        for j in range(len(total_history[i])):
            dian_list.append(total_history[i][j])
            if total_history[i][j]==0:
                fu_list.append(0)
                demand_list.append(0)
            else:
                fuwu_time=data[total_history[i][j]-1][9]/60#服务时间
                fu_list.append(fuwu_time)
                demand_list.append(data[total_history[i][j]-1][8])#需求量
    #print(dian_list)
    for k in range(len(dian_list)-1):
        last=dian_list[k]
        next=dian_list[k+1]
        if last==next:
            dis_list.append(0)
            continue
        else:
            distance=reference[last][next]
            dis_list.append(distance)

    for j in range(len(wijlist)):
        huowu_list.append(0)
        for i in range(len(wijlist[j])):
            huowu_list.append(wijlist[j][i])
    #print("货物变换表：{}".format(huowu_list))
    gx=0
    for k in range(len(dian_list)):
        gx+=p*(demand_list[k]*(1-math.exp(aerfa1*dis_list[k]/v))+huowu_list[k]*(1-math.exp(-aerfa2*fu_list[k])))

    eij=aerfa*sum(dis_list)/v+len(total_history)*250+gx+c_e*(sum(time_list)-sum(fu_list))+ce_*sum(fu_list)
    print("总成本为：{}".format(eij))



#总路线和迭代次数

history,number=rout()
print("迭代次数：{}".format(number))

#分离路线
total_history=one_route(history)
print("路线：{}".format(total_history))
#得出每条路线载货变化列表
wijlist=wij_list(total_history)
#print("货物变换表：{}".format(wijlist))


#分别对应的每条路线所花时间，以及每条路线的发车时间
time_list,time_list_start=time_give(total_history)
#print("每条线路所花时间：{}".format(time_list))
#每条路线的能源消耗
eij_total,distance_list=energy_cost(total_history,wijlist)
print("路线能源消耗：{}".format(eij_total))
energy_judge(eij_total,total_history)