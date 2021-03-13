 
# Travesing through a dictionary


myDict = {'name': 'Edy', 'age': 27, 'address': 'London'}

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
traverseDict(myDict)                  # Time Complexity: O(1)
