# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import random

#weight = np.random.uniform(-1, 1, (2,1))
bias = np.array([1,round(random.uniform(-1,0), 2)])
X1 = np.random.randint(0,2,20)
X2 = np.random.randint(0,2,20)
#X1 = [0,0,1,1]*5
#X2 = [0,1,0,1]*5
learningRate = 0.03

andOutput = X1&X2
orOutput = X1|X2
#andOutput = [0,0,0,1]*5 #Actual Output in AND
#orOutput = [0,1,1,1]*5  #Actual Output in OR
#xorOutput = [0,1,1,0]*5 #Actual Output in XOR

Y = np.zeros(20)
E = np.ones(20)
errRate = 1
W1 = np.zeros(21)
W2 = np.zeros(21)
W1[0] = round(np.random.uniform(-1,1), 2)
W2[0] = round(np.random.uniform(-1,1), 2)


while errRate > 0.3 :   
    err = 0
    for i in range(20):
        Y[i] = np.sign(X1[i]*W1[i]+X2[i]*W2[i]+bias[0]*bias[1])
        
        if Y[i] == -1:
            Y[i] = 0
           
        E[i] =  andOutput[i]- Y[i]
        #E[i] =  orOutput[i]- Y[i]
        
        if E[i] != 0:
            err += 1
        
        W1[i+1] = W1[i] + E[i]*X1[i]*learningRate
        W2[i+1] = W2[i] + E[i]*X2[i]*learningRate
        print("W1: ", W1[i+1])
        print("W2: ", W2[i+1])
        if i == 19:
            W1[0] = W1[i+1]
            W2[0] = W2[i+1]
            errRate = err/20
            
            
print("AND Perceptron: ")
#print("OR Perceptron: ")
print("  Weight1: ",W1[0],"  Weight2: ",W2[0])
print("  ErrorRate: ",errRate)    
