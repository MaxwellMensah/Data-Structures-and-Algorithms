a = [1,2,3]
b = [3,2,1]

def permutation(list1, list2):
    list2.reverse()
    if list1 == list2:
        return True
    else:
        return False

print(permutation(a, b))
