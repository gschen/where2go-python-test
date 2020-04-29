import numpy as np

def distributeCandies(candies,num_people):
    #nums = np.zeros(num_people)
    nums = []
    i=1
    while(candies>=0):
        nums.append(i)
        i+=1
        candies-=i
    return nums



print(distributeCandies(11,4))