# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:57:52 2017

@author: pondjames007
"""

import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.spatial.distance import cdist

#cluCen = random.randint(5,20)
#dataNum = 1000;

cluCen = input("Number of clusters: ")
dataNum = input("Number of data: ")

cluCen = int(cluCen)
dataNum = int(dataNum)

cluster = np.random.randint(0, 10000, (cluCen, 2), dtype = int)

dataSet = np.random.randint(0,10000, (dataNum, 2), dtype = int)

newCen = np.zeros((cluCen, 2))
newGroupCen = np.array([0.0,0.0])
cntRound = 0
while(1):  
    dist = cdist(dataSet, cluster, metric = 'Euclidean')
    minDist = dist.min(1)
    group = dist.argmin(1)
    
    for i in range(cluCen):
        cnt = 0
        newGroupCen = [0,0]
        #print(newGroupCen)
        for j in range(dataNum):
            if group[j] == i:
                newGroupCen += dataSet[j,:]
                cnt += 1 
        if cnt != 0:
            newGroupCen = 1/cnt * newGroupCen
            #print(newGroupCen)
            newCen[i,:] = newCen[i,:] + newGroupCen
    print("------------")
    print(newCen)        
    if(np.array_equal(cluster, newCen)):
        break
    else:
        cluster = newCen
        newCen = np.zeros((cluCen,2))

    plt.plot(dataSet[:,0], dataSet[:,1], 'r.')
    plt.plot(cluster[:,0], cluster[:,1], 'bo')
    plt.axis([0,10000,0,10000])
    plt.show()
    cntRound = cntRound+1
print(cntRound)
