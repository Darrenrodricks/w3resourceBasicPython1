# Write a Python program to find whether a given number
# (accept from the user) is even or odd, print out an appropriate message to the user.

def numChecker(int):
    if int % 2 != 0:
        print("You picked an odd number")
    elif int % 2 == 0:
        print("You picked an even number")

numChecker(40)
numChecker(50)
numChecker(55)
numChecker(87)

