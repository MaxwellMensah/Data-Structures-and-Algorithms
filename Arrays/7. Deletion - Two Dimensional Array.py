import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray) 

# Deleting first row(axis=0) as index is 0       --------> TimeComlexity: O(mn); there is movement to replace/fill in empty address in memory
newTDArray = np.delete(twoDArray, 0, axis=0)    # --------> Space Comlexity: O(1) because extra memory is not required to perform this operation
print(newTDArray)                               # ---------> if you delete the last col or row the timecomplexity becomes O(1) because we don't need to move any row or column

# Deleting second row as index is 1
newTDArray = np.delete(twoDArray, 1, axis=0)
print(newTDArray)

# Deleting first column(axis=1) as index is 0
newTDArray = np.delete(twoDArray, 0, axis=1)
print(newTDArray)

# Deleting second column as index is 1
newTDArray = np.delete(twoDArray, 1, axis=1)
print(newTDArray)