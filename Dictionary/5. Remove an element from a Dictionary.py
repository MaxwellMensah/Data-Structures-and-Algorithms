
# Delete an element from a dictionary

myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}

# Method 1: the pop() method; its that the key as the parameter for the pair
print(myDict.pop('name'))     # ---> it directly return the value deleted when print 
print(myDict)


# Method 2: popitem(); this method does not take any parameter. it selects the values randomly and delete it
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict.popitem())       # --> print the pair deleted 
print(myDict)


# Method 3: clear() method
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
myDict.clear()            # --> deletes all elements in the dictionary
print(myDict)


# Method 4: del keyword
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
del myDict['age']
print(myDict)

#-- OR:
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
del myDict        # --> deletes the entire dictionary.    


# Time Complexxity: O(1), amortized: O(n)
