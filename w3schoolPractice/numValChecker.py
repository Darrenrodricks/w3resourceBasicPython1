# Write a Python program to check if a number is positive, negative or zero.
def num_checker(num):
    if num > 0:
        print("The number you picked is positive.")
    elif num < 0:
        print("The number you picked is negative.")
    elif num == 0:
        print("The number you picked is 0.")


num_checker(10000)
num_checker(100)
num_checker(1)
num_checker(0)
num_checker(-1)
num_checker(-100)
num_checker(-10000)