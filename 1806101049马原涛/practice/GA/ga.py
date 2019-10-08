# -*- coding: utf-8 -*-
import numpy as np
import random
import math
import matplotlib.pyplot as plt


def K_compute(alpha, beta):
    rad_alpha = math.radians(alpha)
    rad_beta = math.radians(beta)
    K = math.sqrt(1 - math.cos(1 - math.cos(rad_alpha))) - \
        math.sqrt(1 - math.cos(rad_beta))
    return K


def Initiall_Pop(Popualation_Size, Chromosome_Length, Chromosome_value_range):
    # 初始化个体
    # Population_size  种群大小
    # Chromosome_length 染色体长度
    # Chromosome_value_range 个体值范围
    Popualation = []
    for iPopualation_Size in range(Popualation_Size):
        temp_Popualation = []
        for iChromosome_Length in range(Chromosome_Length):
            temp = Chromosome_value_range[1][iChromosome_Length] - \
                   Chromosome_value_range[0][iChromosome_Length]
            temp_Popualation.append(np.random.rand() * temp)
        Popualation.append(temp_Popualation)
    return Popualation


def Select_Operation(Pop, Chromosome_Length, Popualation_Size, Pop_FitnV):
    # 对个体进行选择操作
    # Pop 种群
    # Population_size 种群大小
    # Pop_FitnV"

    # 初始化返回的种群和适应度
    Return_Pop = [[0 for i in range(Chromosome_Length)] for j in range(Popualation_Size)]
    Return_FitnV = [0 for i in range(Popualation_Size)]
    # 计算轮盘选择概率
    temp_FitnV = [1 / x for x in Pop_FitnV]
    rate_FitnV = [x / sum(temp_FitnV) for x in temp_FitnV]
    cumsum_FitnV = np.cumsum(rate_FitnV)
    # 轮盘选择
    for iPopualation_Size in range(Popualation_Size):
        select_index = cumsum_FitnV > random.uniform(0, 1)
        Return_Pop[iPopualation_Size][:] = Pop[list(select_index).index(True)][:]
        Return_FitnV[iPopualation_Size] = Pop_FitnV[list(select_index).index(True)]
    return Return_Pop, Return_FitnV


def Cross_Operation(Pop, Popualation_Size, Chromosome_Length, Corss_Probability):
    # 对种群进行交叉操作
    # Pop 种群
    # Population_size 种群大小
    # Chromosome_length 染色体长度
    # cross_probability 交叉概率
    Return_Pop = [[0 for i in range(Chromosome_Length)] for j in range(Popualation_Size)]
    for iPopualation_Size in range(0, Popualation_Size, 2):
        Cross_Pop = Pop[iPopualation_Size:iPopualation_Size + 2][:]
        # 判断是否进行交叉
        if random.random() < Corss_Probability:
            Cross_Index = random.randint(1, Chromosome_Length)
            temp_Pop = Cross_Pop[0][0:Cross_Index]
            Cross_Pop[0][0:Cross_Index] = Cross_Pop[1][0:Cross_Index]
            Cross_Pop[1][0:Cross_Index] = temp_Pop
        Return_Pop[iPopualation_Size][:] = Cross_Pop[0]
        Return_Pop[iPopualation_Size + 1][:] = Cross_Pop[1]
    return Return_Pop


def Mutation_Operation(Pop, Popualation_Size, Chromosome_Length, Chromosome_value_range, Mutation_Probability):
    # 变异操作
    # Population_size 种群大小
    # Chromosome_length 染色体长度
    # Mutation_Probability 变异概率

    # 初始化变异后种群
    Return_Pop = [[0 for i in range(Chromosome_Length)] for j in range(Popualation_Size)]

    # 变异操作
    for iPopualation_Size in range(Popualation_Size):
        for iChromosome_Length in range(Chromosome_Length):
            temp = Pop[iPopualation_Size][iChromosome_Length]
            if random.random() < Mutation_Probability:
                '''u=2*random.random()-1
                if u>0:
                    temp=temp+u*(Chromosome_value_range[1][iChromosome_Length]-temp)
                else:
                    temp=temp+u*(temp-Chromosome_value_range[0][iChromosome_Length])'''
                temp = random.random() * (Chromosome_value_range[1][iChromosome_Length] - Chromosome_value_range[0][
                    iChromosome_Length])
            Return_Pop[iPopualation_Size][iChromosome_Length] = temp;
    return Return_Pop


def Calculation_Fitness(Pop, Popualation_size, K):
    # 计算适应度
    # Pop 种群
    # Popualation_size 种群大小
    FitnV = []
    for iPopualation_Size in range(Popualation_Size):
        # 目标函数
        temp_FitnV = (5 * math.sqrt(2) * Pop[iPopualation_Size][4] / (2 * 3.6)) * (
                    K[0] * Pop[iPopualation_Size][0] + K[1]
                    * Pop[iPopualation_Size][1] + K[2] * Pop[iPopualation_Size][2] + K[3] * Pop[iPopualation_Size][3])
        FitnV.append(np.abs(temp_FitnV))
    return FitnV


Popualation_Size = 30  # 种群大小（可以修改）
Chromosome_Length = 5  # 个体长度（变量个数）

Corss_Probability = 0.9  # 交叉概率（可以修改）（0.8-0.95）
Mutation_Probability = 0.2  # 变异概率（可以修改）（0.05-0.2）

# 计算K
K = []
K.append(K_compute(168, 12))
K.append(K_compute(156, 24))
K.append(K_compute(12, 156))
K.append(K_compute(24, 168))

# 设定值范围
Chromosome_value_range = [[0.01] * Chromosome_Length, [100] * Chromosome_Length]
'''Chromosome_value_range = [[0.01,0.02], [100,200]]'''

# 最大迭代次数
max_iter = 200

Pop = Initiall_Pop(Popualation_Size, Chromosome_Length, Chromosome_value_range)

FitnV = Calculation_Fitness(Pop, Popualation_Size, K)

best_FitnV = []  # 记录最优适应度值
best_Pop = []  # 记录最优个体
best_FitnV.append(min(FitnV))
best_Pop.append(Pop[FitnV.index(min(FitnV))][:])

for iter in range(max_iter):
    # 选择操作
    Pop, FitnV = Select_Operation(Pop, Chromosome_Length, Popualation_Size, FitnV)
    # 交叉操作
    Pop = Cross_Operation(Pop, Popualation_Size, Chromosome_Length, Corss_Probability)
    # 变异操作
    Pop = Mutation_Operation(Pop, Popualation_Size, Chromosome_Length, Chromosome_value_range, Mutation_Probability)
    # 计算适应度
    FitnV = Calculation_Fitness(Pop, Popualation_Size, K)
    # 最优值记录
    if min(FitnV) < best_FitnV[iter]:
        best_FitnV.append(min(FitnV))
        best_Pop.append(Pop[FitnV.index(min(FitnV))][:])
    else:
        best_FitnV.append(best_FitnV[iter])
        best_Pop.append(best_Pop[iter][:])
    print(best_FitnV[iter])
print(best_Pop[iter][:])
plt.figure()
plt.plot(list(range(max_iter + 1)), best_FitnV, '-b')
plt.show()