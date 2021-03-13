
# Search for an element in the dictionary

myDict = {'name': 'Edy', 'age': 26, 'address': 'London'}

def SearchDict(dict, value):
    for key in dict:                         # -- Time Complexity: O(n)
        if dict[key] == value:               # -- Time Complexity: O(1)
            return key, value                # -- Time Complexity: O(1), Space Complexity: O(1) cos additional memory is not required.
    return 'The value does not exist.'

print(SearchDict(myDict, 26))
                                            
