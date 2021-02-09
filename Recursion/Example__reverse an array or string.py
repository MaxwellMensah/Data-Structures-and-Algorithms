# Example: a program to reverse an array or string
# Complete the reverseArray function below.
def reverseArray(a, start, end):
    if start >= end:
        return
    a[start], a[end] = a[end], a[start]
    reverseArray(a, start + 1, end - 1)


a = [1, 4, 3, 2]
print(a)
print("Reversed Array is:")
reverseArray(a, 0, 3)
print(a)
