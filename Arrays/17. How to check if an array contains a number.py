# How to check if an array contains a number in python
import numpy as np 

myArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def findNumber(array, number):
    for i in range(len(array)):
        if array[i] == number:    # if each index value
            print(i)     # returning the index of the value

findNumber(myArray, 20)       # reading starts from 0 for the index