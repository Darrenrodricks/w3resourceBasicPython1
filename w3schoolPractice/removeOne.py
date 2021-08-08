# Write a Python program to remove the first item from a specified list.
def remove_one(list):
    del list[0]
    print(list)


remove_one([1,2,3,4,5,6,7,8,9])
