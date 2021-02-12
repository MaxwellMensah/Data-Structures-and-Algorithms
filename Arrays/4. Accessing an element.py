import numpy as np 

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)  

def accessElements(array, rowIndex, colIndex):    # shdn't exceed the dimensions of the array, len(array)--rows.. len(array[0])--col
    if rowIndex >= len(array) and colIndex >= len(array[0]):   # time complexity ------------------> O(1)              
        print('Incorrect index')                               # time complexity ------------------> O(1)
    else:
        print(array[rowIndex][colIndex])                       # time complexity ------------------> O(1)

accessElements(twoDArray, 1, 2)
