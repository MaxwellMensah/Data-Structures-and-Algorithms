

# Is Unique: Implement an algorithm to determine if a list has all unique characters using a python list.

myList = [1, 20, 30, 44, 5, 56, 57, 8, 19, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]


def isUnique(list):
    checker = []

    for i in list:
        if i in checker:
            print(i)
            return False
        else:
            checker.append(i)
    return True
   
print(isUnique(myList))