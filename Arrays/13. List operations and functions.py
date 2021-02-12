 # List operations / functions
# + Operator
a = [1, 2, 3]
b = [4, 5, 6]

c = a + b
print(c)

# * Operator

a = [0]
a = a * 4
print(a)

a = [0, 1]
a = a * 4
print(a)

# len(): returns count of elements in the List 
a = [0, 1, 2, 3, 4, 5, 6]
print(len(a))

# max(): returns the item with the highest value in the List 
a = [0, 1, 2, 3, 4, 5, 6]
print(max(a))

# min(): returns the item with the lowest value in the List 
a = [0, 1, 2, 3, 4, 5, 6]
print(min(a))

# sum(): returns the sum of all items in the List 
a = [0, 1, 2, 3, 4, 5, 6]
print(sum(a))

# using the combinations of these fuctions above we can use it to find others, like the average of the list.
a = [0, 1, 2, 3, 4, 5, 6]
print(sum(a)/len(a))