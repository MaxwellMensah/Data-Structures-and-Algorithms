# Operations and Built-in Functions

# IN operator
# In operators only checks the keys. We can check values using the values() function
myDict = {'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'cuarto'}      

print('one' in myDict)                                                         # time complexity ------------------> O(1)
print('uno' in myDict.values())


# for operators
myDict = {'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'cuarto'}      

for key in myDict:
    print(key, myDict[key])    # return the key and the value..                   time complexity ------------------> O(1)


#  all() Method. syntax: all(dictionary)...
# the all() method returns true when all elements in the given iterable are true, if not; it returns false

# Case 1: all values are true
myDict = {1: True, 2: True}
print(all(myDict))

# Case 2: all values are false
myDict = {0: False, 1: False}
print(all(myDict))

# Case 3: one values is true, others are false
myDict = {0: True, 1: False, 2: False}
print(all(myDict))

# Case 4: one values is false, others are true
myDict = {0: False, 1: True, 2: True}
print(all(myDict))

# Case 5: one values is false, others are true
myDict = {0: True, 1: False, 2: False}
newDict = {}                           # empty dictionary returns true
print(all(newDict))



# any() Method. syntax: any(dictionary). Returns true if any of the collection is true, if not returns false
myDict = {0: True, 1: False, 2: False}
newDict = {}                           # empty dictionary returns false
print(any(newDict))


# len() Method. syntax: len(dictionary). Return the number of items in the collection
myDict = {0: True, 1: False, 2: False}                   
print(len(myDict))
  

# sorted() Method. syntax: sorted(iterable, reverse, key)
myDict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5} 
print(sorted(myDict))
print(sorted(myDict, reverse=True))

# len based on key
myDict = {'eeeeeeee': 1, 'aaa': 2, 'u': 3, 'oooo': 4, 'ii': 5} 
print(sorted(myDict, key=len))

