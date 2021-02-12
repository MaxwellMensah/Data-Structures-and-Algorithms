
myList = [1,2,3,4,5,6,7]
print(myList)
#  Update 3rd and 4th element
myList[2] = 33
print(myList)
myList[3] = 55
print(myList)

# How Insertion Works
myList = [1,2,3,4,5,6,7]
print(myList)
myList.insert(0, 11)
print(myList)

myList = [1,2,3,4,5,6,7]
myList.insert(4, 15)     # --------> O(n)
print(myList)

# Append
myList = [1,2,3,4,5,6,7]
print(myList)
myList.append(15)         # --------> O(1)
print(myList)

# Extend
newList = [11,12,13,14]
myList.extend(newList)   # --------> O(n), time complexity and space complexity
print(myList)


