# -*- coding: utf-8 -*-
"""
Created on Thu Nov 9 18:57:55 2017

@author: pondjames007
"""

#inputString = "aaaaccccvvvbbbbjjjjj"
outputString = []

inputString = input("Please enter a row of characters: ")

print("Input String: "+ inputString)
runLength = 1

#Encode The String
for idx, char in enumerate(inputString):
    if idx != 0:
        if char == inputString[idx-1]:
            runLength += 1
        else:
            outputString.append((runLength, inputString[idx-1]))
            runLength = 1
    if idx == len(inputString)-1:
        outputString.append((runLength, char))
        
    

print("After Encoding: ")
print(outputString)

decodeStr = []

#Decode The String
for i, (num, char) in enumerate(outputString):
    for j in range(num):
        decodeStr.append(char)

decodeStr = ''.join(decodeStr)        
print("Decoded String: " + decodeStr)        

