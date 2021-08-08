# Write a Python program to input a number, if it is not a number generates an error message.
a = int(input("Please enter a number: "))
if type(a) != int:
    RuntimeError
else:
    print("Your number was {}".format(a))