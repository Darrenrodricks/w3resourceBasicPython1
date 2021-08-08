# Write a Python program to concatenate all elements in a list into a string and return it.

def string_concatenator(list):
    result = ' '
    for items in list:
        result += str(items)
    print(result)

string_concatenator([1,2,3,4,4,5])