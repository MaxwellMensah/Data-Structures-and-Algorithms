
myList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList[0:2]) # same as:

myList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList[:2])

# omitting the second elements
myList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList[1:])

# omitting both elements
myList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList[:])

# updating first two elements
myList = ['a', 'b', 'c', 'd', 'e', 'f']
myList[0:2] = ["x", "y"]
print(myList[:])

# Deleting an element in List using pop() method
myList = ['a', 'b', 'c', 'd', 'e', 'f']
myList.pop(1)                                #  ---------> O(n)
print(myList)

# Without index deletes the last element
myList = ['a', 'b', 'c', 'd', 'e', 'f']
myList.pop()                                  #  ---------> O(1), sinceit del from the last element so no dragging
print(myList)

# Deleting an element in List using pop() method
myList = ['a', 'b', 'c', 'd', 'e', 'f']
myList.pop(2)                                  #  ---------> Time complexity: O(n) ; Space complexity: O(1) 
print(myList)



# Delete() Method
myList = ['a', 'b', 'c', 'd', 'e', 'f']        #  ---------> Time complexity: O(n) ; Space complexity: O(1)
del myList[1]
print(myList)

myList = ['a', 'b', 'c', 'd', 'e', 'f']
del myList[3]
print(myList)

# Multiple deletion (deleting more than one element using slicing)
myList = ['a', 'b', 'c', 'd', 'e', 'f']
del myList[0:2]  # del first two
print(myList)

myList = ['a', 'b', 'c', 'd', 'e', 'f']
del myList[2:4]  # del index two and three
print(myList)




# Remove() Method; deleting the elements itself without knowing any index
myList = ['a', 'b', 'c', 'd', 'e', 'f']
myList.remove('e')                                     #  ---------> Time complexity: O(n) ; Space complexity: O(1)
print(myList)                         # since we can delete from the first elements causing the remaining elements to move.


# NOTE:  You can't slice delete with pop() method and remove. Slicing deletion only works with del function/method