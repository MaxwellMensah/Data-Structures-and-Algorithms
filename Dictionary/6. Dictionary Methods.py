
# clear() - syntax: dictionary.clear()
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
myDict.clear()            # --> deletes all elements in the dictionary
print(myDict)


# copy() - syntax: dictionary.copy()
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
dict = myDict.copy()            # --> make a shallow copy of the dictionary without any modifications.
print(dict)


# fromkeys() - syntax: dictionary.fromkeys(sequence[], value).
""" The fromkeys() method creates a new dictionary from a given sequence of elements with a value provided by the user
it takes two parameters. first parameter is a sequence.  This is the sequence of elements which is to be used as keys from the new dictionary 
and the second parameter is values, which is an optional parameter. the value which is set to each element in the dictionary """

myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
newDict = {}.fromkeys([1,2,3], 0)
print(newDict)


# get() Method - syntax: dictionary.get(key, value). It returns the value for specified key if the key is in the dictionary
# Does not return or ignore anything that is not available  in the dictionary.

myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict.get('age', 27))    # ----> RETURNS 26 since 27 is not available in the dict
print(myDict.get('city', 27))   # ----> if the key does not exist in the dictionary is will return the value we specified


# items () Method - syntax: dictionary.items(). 
# it returns a view object that displays a list of dictionaries k-value type of pairs. Does not take any parameter

myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict.items())


# keys() Method - syntax: dictionary.keys()
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict.keys())


# popitem(); this method does not take any parameter. it selects the values randomly and delete it
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict.popitem())       # --> print the pair deleted 
print(myDict)


# setdefault() - syntax: dictionary.setdefault(key, default_value)
# if the key does not exist, and the default value is not specified it wil return None and 
# if the key does not exist in the dictionary and the defaultvalue is specified, it'll returns the default value  

myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict.setdefault('name', 'added'))   # ---> output: Edy

print(myDict.setdefault('name1', 'added'))   # ---> output: added, and adds the new key name1 to the dict
print(myDict)


# pop() method - syntax: dictionary.pop(); its that the key as the parameter for the pair
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict.pop('name1', 'not'))     # ---> it outputs: not, showing that the key don't exist in the above dict


# values() - syntax: dictionary.values()
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict.values())


# Update() - syntax: dictionary.update(other_dictionary)
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
newDict = {'a':1, 'b':2, 'c':3}

myDict.update(newDict)            # More like joining two dictionaries

print(myDict)

