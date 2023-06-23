## Problem A: SecondHands
from collections import Counter
from utils import CircularQueue, LinkedList
import itertools
import math

data_path = 'Data/watering_well_chapter_1_validation_input.txt'
# data_path = 'Data/watering_well_chapter_1_sample_input.txt'
f = open(data_path,'r')
fw = open('ans.txt', 'w')

def WateringWell(case):
    print(case)
    totalTrees = int(f.readline())
    trees = []
    for tree in range(totalTrees):
        trees.append(tuple(map(int, f.readline().split())))
    
    
    totalWells = int(f.readline())
    wells = []
    for well in range(totalWells):
        wells.append(tuple(map(int, f.readline().split())))
    sum = 0



    # SOL 01
    # def calc_euc_dist(point_1, point_2):
    #     print(point_1[0], " - ", point_2[0],"**2 + ",point_1[1]," - ",point_2[1],"**2")
    #     distance = (point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2
    #     return(distance)

    # for well,tree in itertools.product(wells, trees):
    #     sum += calc_euc_dist(well, tree)
    # return sum

    # SOL 02
    import numpy as np
    from scipy.spatial import distance

    s1 = np.array(wells)
    s2 = np.array(trees)
    sum = int(distance.cdist(s1,s2, 'sqeuclidean').sum())
    return sum
    
   

    

cases = int(f.readline())
for c in range(cases):
    fw.write(f'Case #{c+1}: {WateringWell(c+1)}')
    fw.write('\n')