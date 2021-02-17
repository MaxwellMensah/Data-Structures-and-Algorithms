# Strings and List 

a = 'spam'
b = list(a)
print(b)


# Breaking a string into words
a = 'spam spam spam'
b = a.split()
print(b)

# Delimeter specifies which character to use as word boundary
# Used to convert a string to a list
a = 'spam-spam1-spam2'
delimiter = '-'
b = a.split(delimiter)
print(b)

# Convert list to string
a = 'spam-spam1-spam2'
delimiter = 'a'
b = a.split(delimiter)
print(b)
print(delimiter.join(b))
