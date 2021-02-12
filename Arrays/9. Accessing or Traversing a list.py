shoppingList = ['Milk', 'Cheese', 'Butter']
print(shoppingList[0])

# if an element exist in a lsit 
shoppingList = ['Milk', 'Cheese', 'Butter']
print('Milk' in shoppingList)

shoppingList = ['Milk', 'Cheese', 'Butter']
print('Bread' in shoppingList)

shoppingList = ['Milk', 'Cheese', 'Butter']
print(shoppingList[-1])

shoppingList = ['Milk', 'Cheese', 'Butter']
print(shoppingList[-2])

# Common way to traverse through our element 
shoppingList = ['Milk', 'Cheese', 'Butter']

for i in shoppingList :
    print(i)

# integer list traversing
shoppingList = ['Milk', 'Cheese', 'Butter']

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList[i])

