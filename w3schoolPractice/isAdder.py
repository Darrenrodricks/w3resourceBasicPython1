# Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

def isAdder(str):
    if len(str) >= 2 and str[:2] == "Is":
        print(str)
    else:
        print("Is" + str)

isAdder("monkey")
isAdder("Ismonkey")

