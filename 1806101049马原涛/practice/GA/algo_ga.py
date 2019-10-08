import numpy as np
import matplotlib.pyplot as plt
import math


class GA:
    ''' Genetic Algorithm class
    one population has many chromosomes(individuals)
    one chromosome has many genes
    '''

    # 值定义
    # 种群大小、染色体长度、基因值范围、交叉概率、变异概率
    def __init__(self):
        self.population_size = 30  # one population has 30 chromosomes
        self.chromosome_size = 5  # one chromosome has 5 genes

        # every gene has value between min and max value.
        # 基因值的范围
        self.gene_min_values = [-0.01] * self.chromosome_size
        self.gene_max_valuse = [100] * self.chromosome_size

        self.crossover_probability = 0.9
        self.mutation_probability = 0.2

    # 初始化种群
    def _init_population(self):
        population = []

        for _ in range(self.population_size):
            # 作为单个染色体存储基因值
            one_chromosome = []
            for idx_gene in range(self.chromosome_size):
                # 初始化基因值
                gene_range = self.gene_max_valuse[idx_gene] - self.gene_min_values[idx_gene]
                gene = self.gene_min_values[idx_gene] + gene_range * np.random.rand()
                one_chromosome.append(gene)
            # 染色体加入种群
            population.append(one_chromosome)

        return population

    # 适应性筛选，在计算出旧种群的适应度基础上选出新种群，并计算其适应值
    def _selection(self, population, population_fitness):

        new_population = []
        new_population_fitness = []

        # 1/x used for minimum value, x used for maximum
        # selection strategy is less value, more better.
        # 适应度计算，如[1，2，3，4，5]的适应度为[1/15,2/15,3/15,4/15,5/15]
        # 这里的基因值是取的倒数
        fitness = [1 / x for x in population_fitness]
        fitness_rate = [x / sum(fitness) for x in fitness]
        # 累计概率
        fitness_circle = np.cumsum(fitness_rate)
        # fitness_circle数组内的某位的值等于fitness_rate对应位的值加上fitness_rate内该位前面的所有值
        # 举例：a=[1,2,3,4,5],np.cumsum(a)=[1,3,6,10,15]

        for _ in range(self.population_size):
            # np.random.rand()随机抽取0到1的数
            select_rates = fitness_circle > np.random.rand()
            select_first_index = list(select_rates).index(True)

            new_population.append(population[select_first_index])
            new_population_fitness.append(population_fitness[select_first_index])

        return new_population, new_population_fitness

    # 变异算子
    def _mutation(self, population):
        ''' For every gene, choose some genes probability to mutate.
        '''

        new_population = []

        for chromosome in population:
            new_chromosome = []
            for idx, gene in enumerate(chromosome):

                if np.random.rand() < self.mutation_probability:
                    # 随机变异
                    gene_range = self.gene_max_valuse[idx] - self.gene_min_values[idx]
                    gene = self.gene_min_values[idx] + np.random.rand() * gene_range

                new_chromosome.append(gene)

            new_population.append(new_chromosome)

        return new_population

    # 交叉算子
    def _crossover(self, population):
        ''' flow chart of cross over:
        - select cross over split index.
        - exchange two chromosome with previous split sgement.
        '''

        new_population = []

        for idx in range(0, self.population_size, 2):
            first_chromosome = population[idx]
            second_chromosome = population[idx + 1]

            if np.random.rand() < self.crossover_probability:
                # random select cross index between 0 and the length of chromosome
                # np.random.randint返回一个随机整数
                cross_index = np.random.randint(0, self.chromosome_size)

                cross_segment = first_chromosome[:cross_index]
                first_chromosome[:cross_index] = second_chromosome[:cross_index]
                second_chromosome[:cross_index] = cross_segment

            new_population.append(first_chromosome)
            new_population.append(second_chromosome)

        return new_population

    def _calculate_population_fitness(self, population):

        population_fitness = []

        for chromosome in population:
            population_fitness.append(self._calculate_fitness_value(chromosome))

        return population_fitness

    def _calculate_fitness_value(self, chromosome):
        x0 = chromosome[0]
        x1 = chromosome[1]
        x2 = chromosome[2]
        x3 = chromosome[3]
        x4 = chromosome[4]
        temp = 2 * x0 + 3 * x1 + 4 * x2 + 5 * x3 + 6 * x4
        return temp

    def run(self, iteration_num=500):
        population = self._init_population()
        population_fitness = self._calculate_population_fitness(population)

        best_chromosomes = []
        best_fitness = []

        for idx in range(iteration_num):
            population, population_fitness = self._selection(population, population_fitness)
            population = self._crossover(population)
            population = self._mutation(population)
            population_fitness = self._calculate_population_fitness(population)

            print(idx, min(population_fitness), population[np.argmin(population_fitness)])

            # record every iteration min fitness value
            best_fitness.append(min(population_fitness))
            best_chromosomes.append(population[np.argmin(population_fitness)])

        print(min(best_fitness), best_chromosomes[np.argmin(best_fitness)])
        plt.plot(range(iteration_num), best_fitness, '-b')
        plt.xlabel('iteration num')
        plt.ylabel('fitness value')
        plt.title('Genetic Algorithm')
        plt.show()


if __name__ == '__main__':
    ga = GA()
    ga.run()