# Write a Python program to convert height (in feet and inches) to centimeters.
print("Please enter your height:")
feet = int(input("Please enter how many feet: "))
inches = int(input("Please enter how many inches: "))
x = (feet * 12) + inches
final_val = round(x * 2.54)
print("Your height is {} cm".format(final_val))

