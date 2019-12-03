'''
圣诞活动预热开始啦，汉堡店推出了全新的汉堡套餐。为了避免浪费原料，请你帮他们制定合适的制作计划。
给你两个整数 tomatoSlices 和 cheeseSlices，分别表示番茄片和奶酪片的数目。不同汉堡的原料搭配如下：
巨无霸汉堡：4 片番茄和 1 片奶酪
小皇堡：2 片番茄和 1 片奶酪
请你以 [total_jumbo, total_small]（[巨无霸汉堡总数，小皇堡总数]）的格式返回恰当的制作方案
使得剩下的番茄片 tomatoSlices 和奶酪片 cheeseSlices 的数量都是 0。
如果无法使剩下的番茄片 tomatoSlices 和奶酪片 cheeseSlices 的数量为 0，就请返回 []。
'''
def numOfBurgers(tomatoSlices, cheeseSlices):
    a = min(tomatoSlices, cheeseSlices, tomatoSlices/2)
    if tomatoSlices == 0 and cheeseSlices == 0:
        print([0, 0])
    elif tomatoSlices < cheeseSlices * 2:
        print([])
    else:
        for i in range(a+1):
            for j in range(a+1):
                if i*4 + j*2 == tomatoSlices and i + j == cheeseSlices:
                    print([i, j])
                    a = 0
                    break
        if a != 0:
            print([])