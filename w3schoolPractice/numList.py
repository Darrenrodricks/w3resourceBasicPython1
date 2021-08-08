# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

data = input("Please enter some numbers separated by commas:")
a = data.split(",")
print("List: {}".format(list(a)))
print("Tuple: {}".format(tuple(a)))