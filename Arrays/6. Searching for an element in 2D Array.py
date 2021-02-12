import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray) 

def searchTDArray(array, value):
    for i in range(len(array)):                   # ------------------------> O(mn)
        for j in range(len(array[0])):            # ------------------------> O(n)      time complexity O(n^2)
            if array[i][j] == value:              # ------------------------> O(1)      space complexity O(1)
                return 'The index of the value is '+ str(i) +" "+ str(j)
    return 'Tne element is not found'

print(searchTDArray(twoDArray, 14))
