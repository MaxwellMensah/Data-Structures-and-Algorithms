# Searching fo a element in the list
myList = [10, 20, 30, 40, 50, 60, 70, 80, 90]


# SEARCH METHOD 1: IN operator
if 20 in myList:                # --------> time complexity: O(n)
    print(myList.index(20))  
else:
    print('The values does not exist in the list')



# SEARCH METHOD 2: Linear Search Algorithm
def searchinList(list, value):
    for i in list:                 # --------> time complexity: O(n)
        if i == value:
            return list.index(value)
    return "The value does not exist in the list..."

print(searchinList(myList, 50))
