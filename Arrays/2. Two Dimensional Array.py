# Day 1 - 11,15,10,6
# Day 2 - 10,14,11,5
# Day 3 - 12,17,12,8
# Day 4 - 15,18,14,9

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

newIwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=1) 
print(newIwoDArray)     # Time Complexity O(mn)  

newIwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=0) 
print(newIwoDArray)      # Time Complexity O(mn)

newIwoDArray = np.insert(twoDArray, 1, [[1, 2, 3, 4]], axis=0)  
print(newIwoDArray)      # Time Complexity is O(mn)

newIwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)  
print(newIwoDArray)   # Time Complexity here is O(1) since we're not moving any position to fit an array
